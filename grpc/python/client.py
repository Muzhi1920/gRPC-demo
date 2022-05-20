# -*- coding: utf-8 -*-

import grpc
from proto import rec_pb2,rec_pb2_grpc
import time


def feed_articles(stub):
    user_request = rec_pb2.user_request()
    user_request.user_id = "123"
    user_request.age = 32
    user_request.gender = 1
    user_request.video_nums = 8
    user_request.time_stamp = int(time.time() * 1000)
    user_request.platform = "android"

    # stub call
    res = stub.rec_sys(user_request)
    print('res is {}'.format(res))
    return res


def run():
    """
    client rpc run
    """
    # connect rpc server
    with grpc.insecure_channel('127.0.0.1:8888') as channel:
        # create rpc stub and request
        stub = rec_pb2_grpc.RecSystemStub(channel)
        feed_articles(stub)

if __name__ == '__main__':
    run()
