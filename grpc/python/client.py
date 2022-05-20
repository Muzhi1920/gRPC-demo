# -*- coding: utf-8 -*-

import grpc
from proto import rec_pb2,rec_pb2_grpc
import time


def request_video(stub):
    user_request = rec_pb2.request()
    user_request.user_id = 'zhang san'
    user_request.age = 32
    user_request.gender = 1
    user_request.platform = "android"
    user_request.video_nums = 8

    context = 'test port 4001'

    # stub call
    res = stub.rec_sys(user_request, context)
    print('rec res is {}'.format(res))


def run():
    with grpc.insecure_channel('127.0.0.1:4001') as channel:
        stub = rec_pb2_grpc.RecSystemStub(channel)
        request_video(stub)

if __name__ == '__main__':
    run()
