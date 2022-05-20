# -*- coding: utf-8 -*-

from proto import rec_pb2,rec_pb2_grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
import time


# define return class
class UserRecommendService(rec_pb2_grpc.UserRecommendServicer):

    def user_recommend(self, request, context):
        # request是调用的请求数据对象
        user_id = request.user_id
        channel_id = request.channel_id
        article_num = request.article_num
        time_stamp = request.time_stamp

        response = rec_pb2.ArticleResponse()

        # 手动构造推荐结果，后续对接真实推荐代码
        response.exposure = 'exposure param'
        response.time_stamp = round(time.time() * 1000)
        recommends = []
        for i in range(article_num):
            article = rec_pb2.Article()
            article.track.click = 'click param {}'.format(i + 1)
            article.track.collect = 'collect param {}'.format(i + 1)
            article.track.share = 'share param {}'.format(i + 1)
            article.track.read = 'read param {}'.format(i + 1)
            article.article_id = i + 1
            recommends.append(article)
        response.recommends.extend(recommends)
        ## 返回响应
        return response


def serve():
    """
    rpc服务端启动方法
    """
    # 创建一个rpc服务器
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    # 向服务器中添加被调用的服务方法
    rec_pb2_grpc.add_UserRecommendServicer_to_server(UserRecommendService(), server)

    # 微服务器绑定ip地址和端口
    server.add_insecure_port('127.0.0.1:4001')

    # 启动rpc服务
    server.start()

    # start()不会阻塞，此处需要加上循环睡眠 防止程序退出
    while True:
        time.sleep(10)


if __name__ == '__main__':
    serve()

