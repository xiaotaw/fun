## selfie2anime
基于[taki0112/UGATIT](https://github.com/taki0112/UGATIT/tree/e8efff198e252df0f3a5c936f02e7e7669264b13)创建本地服务

#### 依赖
```bash
# python=2.7 和 tensorflow(r1.8 ~ r1.14)
apt-get install python-dev python-pip
# 需要时，指定tensorflow版本
pip install -U pip tensorflow 

# opencv3
apt-get install libglib2.0-dev
pip install opencv-python==3.2.0.8
# 如果用conda，可以
conda install -c menpo opencv3

# face_recognition
apt-get install cmake
pip install face_recognition

```




#### 通信

json格式的post请求，json示例：json={"test_A_files": "path_to_selfie_image"}

#### 演示
1. 下载checkpoint到UGATIT目录下（注：压缩包4.7G，解压后7.5G） 
```
|--- UGATIT  
    |--- checkpoint  
        |--- .DS_Store  
        |--- UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing  
            |--- checkpoint  
            |--- UGATIT.model-1000000.data-00000-of-00001  
            |--- UGATIT.model-1000000.index  
            |--- UGATIT.model-1000000.meta  
```

2. 准备一张人脸图片(png或jpg格式)，并替换掉selfie2anime_test.py中的示例图片路径，之后：  
本地服务启动：`python2 selfie2anime.py`  
本地服务测试：`python2 selfie2anime_test.py`  
