# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: no_package_name_importer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.twitchtv.twirp.twirptest.no_package_name import no_package_name_pb2 as github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_no__package__name_dot_no__package__name__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='no_package_name_importer.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1eno_package_name_importer.proto\x1aIgithub.com/twitchtv/twirp/twirptest/no_package_name/no_package_name.proto2\x1c\n\x04Svc2\x12\x14\n\x06Method\x12\x04.Msg\x1a\x04.MsgB\x1aZ\x18no_package_name_importerb\x06proto3')
  ,
  dependencies=[github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_no__package__name_dot_no__package__name__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\030no_package_name_importer'))

_SVC2 = _descriptor.ServiceDescriptor(
  name='Svc2',
  full_name='Svc2',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=109,
  serialized_end=137,
  methods=[
  _descriptor.MethodDescriptor(
    name='Method',
    full_name='Svc2.Method',
    index=0,
    containing_service=None,
    input_type=github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_no__package__name_dot_no__package__name__pb2._MSG,
    output_type=github_dot_com_dot_twitchtv_dot_twirp_dot_twirptest_dot_no__package__name_dot_no__package__name__pb2._MSG,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC2)

DESCRIPTOR.services_by_name['Svc2'] = _SVC2

# @@protoc_insertion_point(module_scope)
