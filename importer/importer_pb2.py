# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: importer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.twitchtv.twirp.twirptest.importable import importable_pb2 as github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_importable_dot_importable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='importer.proto',
  package='twirp.twirptest.importer',
  syntax='proto3',
  serialized_pb=_b('\n\x0eimporter.proto\x12\x18twirp.twirptest.importer\x1a?github.com/twitchtv/twirp/twirptest/importable/importable.proto2P\n\x04Svc2\x12H\n\x04Send\x12\x1f.twirp.twirptest.importable.Msg\x1a\x1f.twirp.twirptest.importable.MsgB\nZ\x08importerb\x06proto3')
  ,
  dependencies=[github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_importable_dot_importable__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\010importer'))

_SVC2 = _descriptor.ServiceDescriptor(
  name='Svc2',
  full_name='twirp.twirptest.importer.Svc2',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=109,
  serialized_end=189,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='twirp.twirptest.importer.Svc2.Send',
    index=0,
    containing_service=None,
    input_type=github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_importable_dot_importable__pb2._MSG,
    output_type=github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_importable_dot_importable__pb2._MSG,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC2)

DESCRIPTOR.services_by_name['Svc2'] = _SVC2

# @@protoc_insertion_point(module_scope)
