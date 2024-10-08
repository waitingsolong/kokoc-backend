# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"D\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"?\n\x10RegisterResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"P\n\rLoginResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x12\n\ntoken_type\x18\x03 \x01(\t\",\n\x13RefreshTokenRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"9\n\rTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\ntoken_type\x18\x02 \x01(\t\"3\n\x11\x41ssignRoleRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"%\n\x12\x41ssignRoleResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0eGetUserRequest\x12\r\n\x05token\x18\x01 \x01(\t\"=\n\x0cUserResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t2\xb0\x02\n\x0b\x41uthService\x12\x39\n\x08Register\x12\x15.auth.RegisterRequest\x1a\x16.auth.RegisterResponse\x12\x30\n\x05Login\x12\x12.auth.LoginRequest\x1a\x13.auth.LoginResponse\x12>\n\x0cRefreshToken\x12\x19.auth.RefreshTokenRequest\x1a\x13.auth.TokenResponse\x12?\n\nAssignRole\x12\x17.auth.AssignRoleRequest\x1a\x18.auth.AssignRoleResponse\x12\x33\n\x07GetUser\x12\x14.auth.GetUserRequest\x1a\x12.auth.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=20
  _globals['_REGISTERREQUEST']._serialized_end=88
  _globals['_REGISTERRESPONSE']._serialized_start=90
  _globals['_REGISTERRESPONSE']._serialized_end=153
  _globals['_LOGINREQUEST']._serialized_start=155
  _globals['_LOGINREQUEST']._serialized_end=205
  _globals['_LOGINRESPONSE']._serialized_start=207
  _globals['_LOGINRESPONSE']._serialized_end=287
  _globals['_REFRESHTOKENREQUEST']._serialized_start=289
  _globals['_REFRESHTOKENREQUEST']._serialized_end=333
  _globals['_TOKENRESPONSE']._serialized_start=335
  _globals['_TOKENRESPONSE']._serialized_end=392
  _globals['_ASSIGNROLEREQUEST']._serialized_start=394
  _globals['_ASSIGNROLEREQUEST']._serialized_end=445
  _globals['_ASSIGNROLERESPONSE']._serialized_start=447
  _globals['_ASSIGNROLERESPONSE']._serialized_end=484
  _globals['_GETUSERREQUEST']._serialized_start=486
  _globals['_GETUSERREQUEST']._serialized_end=517
  _globals['_USERRESPONSE']._serialized_start=519
  _globals['_USERRESPONSE']._serialized_end=580
  _globals['_AUTHSERVICE']._serialized_start=583
  _globals['_AUTHSERVICE']._serialized_end=887
# @@protoc_insertion_point(module_scope)
