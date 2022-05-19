# -*- coding: utf-8 -*-

import grpc
import reco_pb2
import reco_pb2_grpc
import time


def feed_articles(stub):
    user_request = reco_pb2.UserRequest()
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
    with grpc.insecure_channel('127.0.0.1:8888') as channel:
        # create rpc stub and request
        stub = reco_pb2_grpc.UserRecommendStub(channel)
        feed_articles(stub)

if __name__ == '__main__':
    run()
