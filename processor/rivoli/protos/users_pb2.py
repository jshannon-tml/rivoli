# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12protos/users.proto\x12\x13rivoli.protos.users\"V\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x32\n\x05roles\x18\x03 \x03(\x0b\x32#.rivoli.protos.users.RoleAssignment\"L\n\x0eRoleAssignment\x12\x11\n\tpartnerId\x18\x01 \x01(\t\x12\'\n\x04role\x18\x02 \x01(\x0b\x32\x19.rivoli.protos.users.Role\"\xd5\x03\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07isAdmin\x18\x03 \x01(\x08\x12\x39\n\x0bpermissions\x18\x04 \x03(\x0e\x32$.rivoli.protos.users.Role.Permission\"\xe6\x02\n\nPermission\x12\x16\n\x12PERMISSION_UNKNOWN\x10\x00\x12\x0f\n\x0bVIEW_CONFIG\x10\x01\x12\x17\n\x13\x45\x44IT_CONFIG_PARTNER\x10\r\x12\x19\n\x15\x45\x44IT_CONFIG_FILETYPES\x10\x0e\x12\x1b\n\x17\x45\x44IT_CONFIG_RECORDTYPES\x10\x0f\x12\x12\n\x0eVIEW_FILE_INFO\x10\x03\x12\x16\n\x12VIEW_ERROR_RECORDS\x10\x04\x12\x14\n\x10VIEW_ALL_RECORDS\x10\x05\x12\x19\n\x15VIEW_SENSITIVE_FIELDS\x10\x06\x12\x1a\n\x16VIEW_UNREDACTED_FIELDS\x10\x07\x12\"\n\x1e\x45\x44IT_VIEWABLE_FILE_AND_RECORDS\x10\x08\x12\x0f\n\x0bWORK_ERRORS\x10\t\x12\x0f\n\x0bUPLOAD_FILE\x10\n\x12\r\n\tLOAD_FILE\x10\x0b\x12\x10\n\x0cPROCESS_FILE\x10\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=43
  _USER._serialized_end=129
  _ROLEASSIGNMENT._serialized_start=131
  _ROLEASSIGNMENT._serialized_end=207
  _ROLE._serialized_start=210
  _ROLE._serialized_end=679
  _ROLE_PERMISSION._serialized_start=321
  _ROLE_PERMISSION._serialized_end=679
# @@protoc_insertion_point(module_scope)
