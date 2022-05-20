# -*- coding: utf-8 -*-

import grpc
from proto import rec_pb2,rec_pb2_grpc
import time


def feed_articles(stub):
    user_request = rec_pb2.UserRequest()
    user_request.user_id = '1'
    user_request.channel_id = 1
    user_request.article_num = 10
    user_request.time_stamp = round(time.time() * 1000)

    # stub call
    ret = stub.user_recommend(user_request)
    print('ret={}'.format(ret))


def run():
    """
    client rpc run
    """
    # connect rpc server
    with grpc.insecure_channel('127.0.0.1:4001') as channel:
        # create rpc stub and request
        stub = rec_pb2_grpc.UserRecommendStub(channel)
        feed_articles(stub)

if __name__ == '__main__':
    run()
