# gRPC-demo

参考[RPC系列之--推荐系统实现方案(python)](https://blog.csdn.net/Jack_yun_feng/article/details/96359444)

1. `pip install grpcio-tools`
2. `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. reco.proto`
3. `python server.py`
4. `python client.py`

