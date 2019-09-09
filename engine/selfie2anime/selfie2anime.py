import argparse
import cgi
import json
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from UGATIT.utils import *
from UGATIT.UGATIT import UGATIT

"""parsing and configuration"""

def parse_args():
    desc = "Tensorflow implementation of U-GAT-IT"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--phase', type=str, default='testA2B', help='[testA2B / testB2A]')
    parser.add_argument('--light', type=str2bool, default=False, help='[U-GAT-IT full version / U-GAT-IT light version]')
    parser.add_argument('--dataset', type=str, default='selfie2anime', help='dataset_name')

    parser.add_argument('--epoch', type=int, default=100, help='The number of epochs to run')
    parser.add_argument('--iteration', type=int, default=10000, help='The number of training iterations')
    parser.add_argument('--batch_size', type=int, default=1, help='The size of batch size')
    parser.add_argument('--print_freq', type=int, default=1000, help='The number of image_print_freq')
    parser.add_argument('--save_freq', type=int, default=1000, help='The number of ckpt_save_freq')
    parser.add_argument('--decay_flag', type=str2bool, default=True, help='The decay_flag')
    parser.add_argument('--decay_epoch', type=int, default=50, help='decay epoch')

    parser.add_argument('--lr', type=float, default=0.0001, help='The learning rate')
    parser.add_argument('--GP_ld', type=int, default=10, help='The gradient penalty lambda')
    parser.add_argument('--adv_weight', type=int, default=1, help='Weight about GAN')
    parser.add_argument('--cycle_weight', type=int, default=10, help='Weight about Cycle')
    parser.add_argument('--identity_weight', type=int, default=10, help='Weight about Identity')
    parser.add_argument('--cam_weight', type=int, default=1000, help='Weight about CAM')
    parser.add_argument('--gan_type', type=str, default='lsgan', help='[gan / lsgan / wgan-gp / wgan-lp / dragan / hinge]')

    parser.add_argument('--smoothing', type=str2bool, default=True, help='AdaLIN smoothing effect')

    parser.add_argument('--ch', type=int, default=64, help='base channel number per layer')
    parser.add_argument('--n_res', type=int, default=4, help='The number of resblock')
    parser.add_argument('--n_dis', type=int, default=6, help='The number of discriminator layer')
    parser.add_argument('--n_critic', type=int, default=1, help='The number of critic')
    parser.add_argument('--sn', type=str2bool, default=True, help='using spectral norm')

    parser.add_argument('--img_size', type=int, default=256, help='The size of image')
    parser.add_argument('--img_ch', type=int, default=3, help='The size of image channel')
    parser.add_argument('--augment_flag', type=str2bool, default=True, help='Image augmentation use or not')

    parser.add_argument('--checkpoint_dir', type=str, default='UGATIT/checkpoint',
                        help='Directory name to save the checkpoints')
    parser.add_argument('--result_dir', type=str, default='UGATIT/results',
                        help='Directory name to save the generated images')
    parser.add_argument('--log_dir', type=str, default='UGATIT/logs',
                        help='Directory name to save training logs')
    parser.add_argument('--sample_dir', type=str, default='UGATIT/samples',
                        help='Directory name to save the samples on training')

    parser.add_argument('--a2b_host', type=str, default='0.0.0.0',
                        help='selfie2anime engine listen host')

    parser.add_argument('--a2b_port', type=int, default='6201',
                        help='selfie2anime engine listen port')

    return check_args(parser.parse_args())

"""checking arguments"""
def check_args(args):
    # --checkpoint_dir
    check_folder(args.checkpoint_dir)

    # --result_dir
    check_folder(args.result_dir)

    # --result_dir
    check_folder(args.log_dir)

    # --sample_dir
    check_folder(args.sample_dir)

    # --epoch
    try:
        assert args.epoch >= 1
    except:
        print('number of epochs must be larger than or equal to one')

    # --batch_size
    try:
        assert args.batch_size >= 1
    except:
        print('batch size must be larger than or equal to one')
    return args


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # datatype
        ctype, pdict = cgi.parse_header(self.headers['content-type'])

        if ctype == 'application/json':
            length = int(self.headers['content-length'])
            post_values = json.loads(self.rfile.read(length))
            # do something
            if "test_A_files" in post_values:
                sample_file = post_values["test_A_files"]
                print(sample_file)
                sample_image = np.asarray(load_test_data(sample_file, size=gan.img_size))
                fake_img = sess.run(gan.test_fake_B, feed_dict = {gan.test_domain_A : sample_image})
                
                path, ext = os.path.splitext(sample_file)
                image_path = path + "-converted" + ext
                #image_path = os.path.join(gan.result_dir, os.path.basename(sample_file))
                save_images(fake_img, [1, 1], image_path)
            else:
                pass
            print(post_values)

            req_dic = {"fake_B_files": image_path}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(req_dic))

        else:
            self.send_error(415, "Only json data is spported")
            return


"""main"""
if __name__ == "__main__":
    # parse arguments
    args = parse_args()
    if args is None:
      exit()

    # open session
    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True)) as sess:
        gan = UGATIT(sess, args)

        # build graph
        gan.build_model()

        # show network architecture
        show_all_variables()

        if args.phase == 'testA2B' :
            tf.global_variables_initializer().run()
            
            gan.saver = tf.train.Saver()
            could_load, checkpoint_counter = gan.load(gan.checkpoint_dir)
            if could_load :
                print(" [*] Load SUCCESS")
            else :
                print(" [!] Load failed...")    

            gan.result_dir = os.path.join(gan.result_dir, gan.model_dir)
            check_folder(gan.result_dir)
            
            server = HTTPServer((args.a2b_host, args.a2b_port), RequestHandler)
            print("Starting server, use <Ctrl+c> to stop")
            server.serve_forever()
            
        elif args.phase == 'testB2A': 
            pass
            print(" [*] TestA2B finished!")
        else:
            print("Not supported: %s" % args.phase)



