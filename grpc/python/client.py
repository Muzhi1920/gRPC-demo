import grpc
from proto import rec_pb2,rec_pb2_grpc
import time


def get_videos(stub):
    # create user info request
    user_request = rec_pb2.user_request()
    user_request.user_id = "123"
    user_request.age = 32
    user_request.gender = 1
    user_request.video_nums = 8
    user_request.time_stamp = int(time.time() * 1000)
    user_request.platform = "android"

    # call stub service func
    res = stub.rec_sys(user_request) # 在client中调用server中实现的`rec_sys`方法
    print('rec res is {}'.format(res))
    return res


def run():
    with grpc.insecure_channel('127.0.0.1:8888') as channel:
        stub = rec_pb2_grpc.RecSystemStub(channel) # 使用协议的pkg，通过pb定义得到该stub对象
        get_videos(stub)


if __name__ == '__main__':
    run()
