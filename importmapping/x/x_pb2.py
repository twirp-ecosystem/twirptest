# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: x/x.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from y import y_pb2 as y_dot_y__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='x/x.proto',
  package='twirp.twirptest.importmapping.x',
  syntax='proto3',
  serialized_pb=_b('\n\tx/x.proto\x12\x1ftwirp.twirptest.importmapping.x\x1a\ty/y.proto2\\\n\x04Svc1\x12T\n\x04Send\x12%.twirp.twirptest.importmapping.y.MsgY\x1a%.twirp.twirptest.importmapping.y.MsgYB\x03Z\x01xb\x06proto3')
  ,
  dependencies=[y_dot_y__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\001x'))

_SVC1 = _descriptor.ServiceDescriptor(
  name='Svc1',
  full_name='twirp.twirptest.importmapping.x.Svc1',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=57,
  serialized_end=149,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='twirp.twirptest.importmapping.x.Svc1.Send',
    index=0,
    containing_service=None,
    input_type=y_dot_y__pb2._MSGY,
    output_type=y_dot_y__pb2._MSGY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC1)

DESCRIPTOR.services_by_name['Svc1'] = _SVC1

# @@protoc_insertion_point(module_scope)
