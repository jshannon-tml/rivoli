# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protos/config.proto\x12\x14rivoli.protos.config\"\xdc\x01\n\x07Partner\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x41\n\nstaticTags\x18\x04 \x03(\x0b\x32-.rivoli.protos.config.Partner.StaticTagsEntry\x12\x31\n\tfileTypes\x18\x05 \x03(\x0b\x32\x1e.rivoli.protos.config.FileType\x1a\x31\n\x0fStaticTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x07\n\x08\x46ileType\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x35\n\x06\x66ormat\x18\x04 \x01(\x0e\x32%.rivoli.protos.config.FileType.Format\x12\x13\n\x0b\x66ileMatches\x18\x05 \x03(\t\x12\x1a\n\x12\x66ilenameDateFormat\x18\r \x01(\t\x12\x1a\n\x12\x66ilenameDateRegexp\x18\x08 \x01(\t\x12\x1a\n\x12\x66ilenameTagRegexps\x18\x0c \x03(\t\x12\x42\n\nstaticTags\x18\x0b \x03(\x0b\x32..rivoli.protos.config.FileType.StaticTagsEntry\x12\x11\n\thasHeader\x18\x0f \x01(\x08\x12\x1a\n\x12\x64\x65limitedSeparator\x18\x10 \x01(\t\x12G\n\x0freferencedFiles\x18\x0e \x03(\x0b\x32..rivoli.protos.config.FileType.ReferencedFiles\x12\x43\n\rrequireReview\x18\t \x01(\x0e\x32,.rivoli.protos.config.FileType.RequireReview\x12\x35\n\x0brecordTypes\x18\x07 \x03(\x0b\x32 .rivoli.protos.config.RecordType\x12\x37\n\x0c\x64\x65stinations\x18\n \x03(\x0b\x32!.rivoli.protos.config.Destination\x1a\x31\n\x0fStaticTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x13\x44\x65limitedFileFormat\x12\x11\n\thasHeader\x18\x01 \x01(\t\x12\x11\n\tdelimiter\x18\x02 \x01(\t\x1a\x41\n\x0fReferencedFiles\x12\x12\n\nfileTypeId\x18\x01 \x01(\t\x12\x1a\n\x12requireMatchedDate\x18\x02 \x01(\x08\"P\n\x06\x46ormat\x12\x12\n\x0e\x46ORMAT_UNKNOWN\x10\x00\x12\x17\n\x13\x46LAT_FILE_DELIMITED\x10\x01\x12\x19\n\x15\x46LAT_FILE_FIXED_WIDTH\x10\x02\"S\n\rRequireReview\x12\x13\n\x0fREQUIRE_UNKNOWN\x10\x00\x12\x17\n\x13INGESTION_ON_ERRORS\x10\x01\x12\x14\n\x10INGESTION_ALWAYS\x10\x02\"\x93\x03\n\nRecordType\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rrecordMatches\x18\x04 \x03(\t\x12\x33\n\nfieldTypes\x18\x05 \x03(\x0b\x32\x1f.rivoli.protos.config.FieldType\x12:\n\x0csuccessCheck\x18\x06 \x01(\x0b\x32$.rivoli.protos.config.FunctionConfig\x12\x34\n\x06upload\x18\x07 \x01(\x0b\x32$.rivoli.protos.config.FunctionConfig\x12\x36\n\x08rollback\x18\n \x01(\x0b\x32$.rivoli.protos.config.FunctionConfig\x12\x39\n\x0bvalidations\x18\x08 \x03(\x0b\x32$.rivoli.protos.config.FunctionConfig\x12:\n\x0c\x64\x65stinations\x18\t \x03(\x0b\x32$.rivoli.protos.config.FunctionConfig\"\xbd\x02\n\tFieldType\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bisSharedKey\x18\x0b \x01(\x08\x12\x13\n\x0bisSensitive\x18\t \x01(\x08\x12\x36\n\x08renderer\x18\n \x01(\x0b\x32$.rivoli.protos.config.FunctionConfig\x12\x13\n\tcharRange\x18\x05 \x01(\tH\x00\x12\x16\n\x0cheaderColumn\x18\x06 \x01(\tH\x00\x12\x15\n\x0b\x63olumnIndex\x18\x07 \x01(\x05H\x00\x12\x39\n\x0bvalidations\x18\x08 \x03(\x0b\x32$.rivoli.protos.config.FunctionConfigB\x10\n\x0e\x66ield_location\"D\n\x0e\x46unctionConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfunctionId\x18\x02 \x01(\t\x12\x12\n\nparameters\x18\x03 \x03(\t\"\xd5\x01\n\x0b\x44\x65stination\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.rivoli.protos.config.Destination.DestinationType\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12\x11\n\tautomatic\x18\x04 \x01(\x08\"T\n\x0f\x44\x65stinationType\x12\x17\n\x13\x44\x45STINATION_UNKNOWN\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x02\x12\x10\n\x0cPROGRAMMATIC\x10\x03\x12\x08\n\x04\x46ILE\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARTNER_STATICTAGSENTRY._options = None
  _PARTNER_STATICTAGSENTRY._serialized_options = b'8\001'
  _FILETYPE_STATICTAGSENTRY._options = None
  _FILETYPE_STATICTAGSENTRY._serialized_options = b'8\001'
  _PARTNER._serialized_start=46
  _PARTNER._serialized_end=266
  _PARTNER_STATICTAGSENTRY._serialized_start=217
  _PARTNER_STATICTAGSENTRY._serialized_end=266
  _FILETYPE._serialized_start=269
  _FILETYPE._serialized_end=1196
  _FILETYPE_STATICTAGSENTRY._serialized_start=217
  _FILETYPE_STATICTAGSENTRY._serialized_end=266
  _FILETYPE_DELIMITEDFILEFORMAT._serialized_start=903
  _FILETYPE_DELIMITEDFILEFORMAT._serialized_end=962
  _FILETYPE_REFERENCEDFILES._serialized_start=964
  _FILETYPE_REFERENCEDFILES._serialized_end=1029
  _FILETYPE_FORMAT._serialized_start=1031
  _FILETYPE_FORMAT._serialized_end=1111
  _FILETYPE_REQUIREREVIEW._serialized_start=1113
  _FILETYPE_REQUIREREVIEW._serialized_end=1196
  _RECORDTYPE._serialized_start=1199
  _RECORDTYPE._serialized_end=1602
  _FIELDTYPE._serialized_start=1605
  _FIELDTYPE._serialized_end=1922
  _FUNCTIONCONFIG._serialized_start=1924
  _FUNCTIONCONFIG._serialized_end=1992
  _DESTINATION._serialized_start=1995
  _DESTINATION._serialized_end=2208
  _DESTINATION_DESTINATIONTYPE._serialized_start=2124
  _DESTINATION_DESTINATIONTYPE._serialized_end=2208
# @@protoc_insertion_point(module_scope)
