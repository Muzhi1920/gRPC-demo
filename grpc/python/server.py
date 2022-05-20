# -*- coding: utf-8 -*-

from proto import rec_pb2,rec_pb2_grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
import time


# define return class
class RecSystemService(rec_pb2_grpc.RecSystemServicer):

    def rec_sys(self, request, context):
        # request是调用的请求数据对象

        user_id = request.user_id
        age = request.age
        video_nums = request.video_nums
        time_stamp = request.time_stamp

        print("rpc log : cur info is {}, ctx is {}".format(request, context))
        response = rec_pb2.VideoResponse()
        response.impression = 'impression'
        response.time_stamp = round(time.time() * 1000)
        recsys_res = []
        for i in range(video_nums):
            video = rec_pb2.Video()
            video.meta.cover = 'cover param {}'.format(i + 1)
            video.meta.title = 'title param {}'.format(i + 1)
            video.meta.up = 'up param {}'.format(i + 1)
            video.meta.tag = 'tag param {}'.format(i + 1)
            video.video_id = i + 1
            recsys_res.append(video)
        response.recsys_res.extend(recsys_res)
        ## 返回响应
        return response


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    rec_pb2_grpc.add_RecSystemServicer_to_server(RecSystemService(), server)

    server.add_insecure_port('127.0.0.1:8888')

    server.start()
    print('start ok')
    while True:
        print('running')
        time.sleep(10)


if __name__ == '__main__':
    serve()
