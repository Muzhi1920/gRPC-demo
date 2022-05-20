# gRPC-demo

参考[RPC系列之--推荐系统实现方案(python)](https://blog.csdn.net/Jack_yun_feng/article/details/96359444)

## CPP




## Python
0. `cd python`
1. 编译proto文件：`python -m grpc_tools.protoc -I=./ --python_out=./ --grpc_python_out=./ ./proto/rec.proto`
2. `python server.py`
3. `python client.py`

