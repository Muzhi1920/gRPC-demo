# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import rec_pb2 as proto_dot_rec__pb2


class RecSystemStub(object):
    """
    对request和response建立gRPC服务链接
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.rec_sys = channel.unary_unary(
                '/RecSystem/rec_sys',
                request_serializer=proto_dot_rec__pb2.request.SerializeToString,
                response_deserializer=proto_dot_rec__pb2.VideoResponse.FromString,
                )


class RecSystemServicer(object):
    """
    对request和response建立gRPC服务链接
    """

    def rec_sys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecSystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'rec_sys': grpc.unary_unary_rpc_method_handler(
                    servicer.rec_sys,
                    request_deserializer=proto_dot_rec__pb2.request.FromString,
                    response_serializer=proto_dot_rec__pb2.VideoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RecSystem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecSystem(object):
    """
    对request和response建立gRPC服务链接
    """

    @staticmethod
    def rec_sys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RecSystem/rec_sys',
            proto_dot_rec__pb2.request.SerializeToString,
            proto_dot_rec__pb2.VideoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
