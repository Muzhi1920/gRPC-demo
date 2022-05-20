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
        user_age = request.age
        user_gender = request.gender
        user_platform = request.platform
        video_nums = request.video_nums

        print('log context :{}, cur info is : {}'.format(context, ','.join([user_id,user_age,user_gender,user_platform])))

        response = rec_pb2.VideoResponse()
        # 手动构造推荐结果，后续对接真实推荐代码
        response.impression = 'impression param' # 填充response上下文信息
        response.time_stamp = round(time.time() * 1000)
        mock_rec_res = []
        for i in range(video_nums):
            video = rec_pb2.Video()
            video.Meta.cover = 'video meta info cover : {}'.format(i + 1)
            video.Meta.title = 'video meta info title : {}'.format(i + 1)
            video.Meta.up = 'video meta info up : {}'.format(i + 1)
            video.Meta.tag = 'video meta info tag : {}'.format(i + 1)
            video.video_id = i + 10000
            mock_rec_res.append(video)
        response.mock_rec_res.extend(mock_rec_res)
        ## 返回响应
        return response


def run():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rec_pb2_grpc.add_RecSystemServicer_to_server(RecSystemService(), server)
    server.add_insecure_port('127.0.0.1:4001')
    print("start server...")
    server.start()
    while True:
        time.sleep(10)


if __name__ == '__main__':
    run()

