# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/rec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fproto/rec.proto\"]\n\x07request\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0e\n\x06gender\x18\x03 \x01(\x05\x12\x10\n\x08platform\x18\x04 \x01(\x05\x12\x12\n\nvideo_nums\x18\x05 \x01(\x05\"=\n\x04Meta\x12\r\n\x05\x63over\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\n\n\x02up\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x04 \x01(\t\".\n\x05Video\x12\x10\n\x08video_id\x18\x01 \x01(\x03\x12\x13\n\x04Meta\x18\x02 \x01(\x0b\x32\x05.Meta\"Q\n\rVideoResponse\x12\x12\n\nimpression\x18\x01 \x01(\t\x12\x12\n\ntime_stamp\x18\x02 \x01(\x03\x12\x18\n\x08rec_algo\x18\x03 \x03(\x0b\x32\x06.Video22\n\tRecSystem\x12%\n\x07rec_sys\x12\x08.request\x1a\x0e.VideoResponse\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['request']
_META = DESCRIPTOR.message_types_by_name['Meta']
_VIDEO = DESCRIPTOR.message_types_by_name['Video']
_VIDEORESPONSE = DESCRIPTOR.message_types_by_name['VideoResponse']
request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'proto.rec_pb2'
  # @@protoc_insertion_point(class_scope:request)
  })
_sym_db.RegisterMessage(request)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), {
  'DESCRIPTOR' : _META,
  '__module__' : 'proto.rec_pb2'
  # @@protoc_insertion_point(class_scope:Meta)
  })
_sym_db.RegisterMessage(Meta)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), {
  'DESCRIPTOR' : _VIDEO,
  '__module__' : 'proto.rec_pb2'
  # @@protoc_insertion_point(class_scope:Video)
  })
_sym_db.RegisterMessage(Video)

VideoResponse = _reflection.GeneratedProtocolMessageType('VideoResponse', (_message.Message,), {
  'DESCRIPTOR' : _VIDEORESPONSE,
  '__module__' : 'proto.rec_pb2'
  # @@protoc_insertion_point(class_scope:VideoResponse)
  })
_sym_db.RegisterMessage(VideoResponse)

_RECSYSTEM = DESCRIPTOR.services_by_name['RecSystem']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=19
  _REQUEST._serialized_end=112
  _META._serialized_start=114
  _META._serialized_end=175
  _VIDEO._serialized_start=177
  _VIDEO._serialized_end=223
  _VIDEORESPONSE._serialized_start=225
  _VIDEORESPONSE._serialized_end=306
  _RECSYSTEM._serialized_start=308
  _RECSYSTEM._serialized_end=358
# @@protoc_insertion_point(module_scope)