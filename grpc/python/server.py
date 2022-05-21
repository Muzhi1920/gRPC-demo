from proto import rec_pb2,rec_pb2_grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
import time


class RecSystemService(rec_pb2_grpc.RecSystemServicer):

    def rec_sys(self, request, context):
        # parse user request info
        user_id = request.user_id
        age = request.age
        video_nums = request.video_nums
        time_stamp = request.time_stamp
        print("rpc log : uid is {}, age is {}, time_stamp is {}, ctx is {}".format(user_id, age, time_stamp, context))

        # make mock rec res
        response = rec_pb2.VideoResponse()
        response.impression = 'impression'
        response.time_stamp = round(time.time() * 1000)
        recsys_res = []
        for i in range(1, video_nums + 1):
            video = rec_pb2.Video()
            video.meta.cover = 'cover_{}'.format(i)
            video.meta.title = 'title_{}'.format(i)
            video.meta.up = 'uploader_{}'.format(i)
            video.meta.tag = 'tag_{}'.format(i)
            video.video_id = i * 1000
            recsys_res.append(video)
        response.recsys_res.extend(recsys_res)

        return response


def run():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rec_pb2_grpc.add_RecSystemServicer_to_server(RecSystemService(), server)
    server.add_insecure_port('127.0.0.1:8888')

    server.start()
    print('start ok')
    while True:
        print('server is running...')
        time.sleep(10)


if __name__ == '__main__':
    run()
