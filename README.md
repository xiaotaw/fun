# FUN Project

### 概述
1. 服务器本地端口6200/6201
2. 接收web请求，处理数据后返回
3. 数据处理，可能需要一个守护进程。例如：加载资源和初始化需要5分钟，处理一张图片需要1秒；不能接收到图片后，再启动处理图片的进程。未解决这类问题，采用unix domain socket。


### 使用unix domain socket构建本地服务的demo示例
1. `cd engine`
2. 启动服务`python2 engine_demo.py`，当前路径下会生成demo_socket。
3. 另开一个终端，启动测试`python2 engine_demo_test.py`，脚本向demo_socket发送"test message"。
4. 服务端收到"test message"后，转成大写"TEST MESSAGE"，发送回客户端。

