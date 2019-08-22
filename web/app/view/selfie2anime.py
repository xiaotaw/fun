# encoding: utf-8

import hashlib
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, current_app, abort

bp = Blueprint('selfie2anime', __name__, url_prefix='/selfie2anime')

ALLOW_FMTS = ('png', 'jpg', 'jpeg')


def save_image(image):
    fname, ffmt = image.filename.rsplit('.', 1)
    if not fname:
        flash('文件名缺失')
        raise ValueError
    if ffmt.lower() not in ALLOW_FMTS:
        flash('目前仅支持 png jpg jpeg 格式的图片哦')
        raise ValueError
    ip = request.remote_addr
    if not ip:
        abort(403)

    app_dir = current_app.config['APP_DIR']
    img_dir = current_app.config['SELFIE2ANIME_DIR']

    fname = secure_filename(fname)
    fname = hashlib.md5(ip + fname).hexdigest() + '.%s' % ffmt
    image.save(app_dir + img_dir + fname)
    return img_dir + fname


@bp.route('/', methods=['GET', 'POST'])
def index():
    converted = False
    if request.method == 'GET':
        return render_template('selfie2anime.html', **locals())

    image = request.files.get('image')
    if not image:
        flash('请上传你的一张自拍照哦')
        return render_template('selfie2anime.html', **locals())

    converted = True
    # todo: 移除图片前面的 /static/
    original_img_path = save_image(image)[8:]
    converted_img_path = original_img_path
    return render_template('selfie2anime.html', **locals())
