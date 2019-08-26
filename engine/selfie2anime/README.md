## selfie2anime
基于[taki0112/UGATIT](https://github.com/taki0112/UGATIT/tree/e8efff198e252df0f3a5c936f02e7e7669264b13)

#### 依赖

python=2.7, tensorflow=1.8(1.8和1.14版本都可以), opencv3

* opencv3的简易安装：`conda install -c menpo opencv3`

### 演示
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
