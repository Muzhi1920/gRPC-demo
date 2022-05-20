# gRPC-demo

参考[RPC系列之--推荐系统实现方案(python)](https://blog.csdn.net/Jack_yun_feng/article/details/96359444)

## protobuf
github：https://github.com/protocolbuffers/protobuf
针对特定语言的protobuf，下载后编译使用。下载`all`版本适合多种语言编译时间较长

- protobuf-all-v
- protobuf-cpp-v
- protobuf-python-v   **conda/pip**
- protobuf-java-v

安装参考：https://github.com/protocolbuffers/protobuf/tree/main/src

## Python

### requerments
`pip install grpcio-tools`

### run
0. `cd python`
1. 编译proto文件：`python -m grpc_tools.protoc -I=./ --python_out=./ --grpc_python_out=./ ./proto/rec.proto`
2. `python server.py`
3. `python client.py`


## Java
- protobuf-jave-version.jar
- other jars needed

### maven run
```shell
protoc -I./ --java_out=./ ./proto/rec.proto

javac -cp ./protobuf-java-x.jar ./Rec.java # 指定该java类需要protobuf的java版本否则报错

jar cvf rec.jar ./*.class # 打压缩包：javac -cvf xxx.jar xxx

mvn deploy:deploy-file # maven管理发布jar
-DgroupId=com.rec
-DartifactId=rec
-Dversion=1.0
-Dpackaging=jar
-Dfile=rec.jar
-Durl=http://path/jar_lib
-DrepositoryId=release

```


## CPP [TODO]

`protoc -I=./ --cpp_out=./ ./proto/rec.proto`

