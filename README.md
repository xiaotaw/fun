# FUN Project

### 概述
1. 服务器本地端口6200/6201
2. 接收web请求，处理数据后返回
3. 数据处理，可能需要一个守护进程。例如：加载资源和初始化需要5分钟，处理一张图片需要1秒；不能接收到图片后，再启动处理图片的进程。为解决这类问题，采用unix domain socket进行本地进程之间通信。


### 使用unix domain socket构建本地服务的demo示例
1. `cd engine`
2. 启动服务`python2 engine_demo.py`，当前路径下会生成demo_socket。
3. 另开一个终端，启动测试`python2 engine_demo_test.py`，脚本向demo_socket发送"test message"。
4. 服务端收到"test message"后，转成大写"TEST MESSAGE"，发送回客户端。


### UGATIT's selfie2anime
1. pre-trained model



2. dataset collection:  

source|links|status
-|-|-
[official release](https://github.com/taki0112/UGATIT)|https://drive.google.com/file/d/1xOWj1UVgp6NKMT3HbPhBbtq2A4EDkghF/view?usp=sharing| tobe download
[selfie](https://www.crcv.ucf.edu/data/Selfie/)|https://www.crcv.ucf.edu/data/Selfie/Selfie-dataset.tar.gz | downloaded
[Anime Face](https://github.com/Mckinsey666/Anime-Face-Dataset)|https://drive.google.com/file/d/1HG7YnakUkjaxtNMclbl2t5sJwGLcHYsI/view?usp=sharing| tobe download
[This Waifu Does Not Exist](https://www.gwern.net/TWDNE#downloads) | https://mega.nz/#!aPRFDKaC!FDpQi_FEPK443JoRBEOEDOmlLmJSblKFlqZ1A1XPt2Y， | tobe download
<blank> |https://mega.nz/#!3qJ0DKKI!uYCz7QpD0NdvBJQ_QdjC6M9L2_UuCHDmF9lAqeSkK2E，| tobe download
<blank> |https://www.gwern.net/docs/ai/2019-02-28-thiswaifudoesnotexist-textsnippets.tar.xz  | downloaded
