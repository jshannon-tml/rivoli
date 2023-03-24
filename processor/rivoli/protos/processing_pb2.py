# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/processing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protos/processing.proto\x12\x18rivoli.protos.processing\"\x9b\x06\n\x04\x46ile\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\tpartnerId\x18\x0f \x01(\t\x12\x18\n\x10\x64\x65velopment_file\x18\x12 \x01(\x08\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x11\n\tsizeBytes\x18\x03 \x01(\x04\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x10\n\x08location\x18\x0b \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\r\x12\x0f\n\x07updated\x18\x05 \x01(\r\x12\x35\n\x06status\x18\x06 \x01(\x0e\x32%.rivoli.protos.processing.File.Status\x12\x16\n\x0erequiresReview\x18\t \x01(\x08\x12\x12\n\nfileTypeId\x18\x07 \x01(\t\x12\x15\n\rheaderColumns\x18\x10 \x03(\t\x12\x10\n\x08\x66ileDate\x18\x11 \x01(\t\x12\x36\n\x04tags\x18\r \x03(\x0b\x32(.rivoli.protos.processing.File.TagsEntry\x12\x34\n\x03log\x18\x08 \x03(\x0b\x32\'.rivoli.protos.processing.ProcessingLog\x12\x34\n\x05stats\x18\x0e \x01(\x0b\x32%.rivoli.protos.processing.RecordStats\x12\x34\n\x05times\x18\x13 \x01(\x0b\x32%.rivoli.protos.processing.RecordTimes\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe3\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x07\n\x03NEW\x10\x05\x12\x0b\n\x07LOADING\x10\n\x12\n\n\x06LOADED\x10\x0f\x12\x0b\n\x07PARSING\x10\x14\x12\n\n\x06PARSED\x10\x19\x12\x0e\n\nVALIDATING\x10\x1e\x12\r\n\tVALIDATED\x10#\x12\x0f\n\x0b\x41GGREGATING\x10(\x12\x0e\n\nAGGREGATED\x10-\x12\x1e\n\x1aWAITING_APPROVAL_TO_UPLOAD\x10\x32\x12\r\n\tUPLOADING\x10\x37\x12\x0c\n\x08UPLOADED\x10<\x12\r\n\tCOMPLETED\x10\x46\"\xf5\x08\n\x06Record\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x42\n\nrecordType\x18\x03 \x01(\x0e\x32..rivoli.protos.processing.Record.RecordTypeRef\x12\x37\n\x06status\x18\x05 \x01(\x0e\x32\'.rivoli.protos.processing.Record.Status\x12\x11\n\tretriable\x18\x11 \x01(\x08\x12\x11\n\tsharedKey\x18\x0b \x01(\t\x12\x0f\n\x07rawLine\x18\x06 \x01(\t\x12\x12\n\nrawColumns\x18\x07 \x03(\t\x12H\n\x0cparsedFields\x18\x08 \x03(\x0b\x32\x32.rivoli.protos.processing.Record.ParsedFieldsEntry\x12N\n\x0fvalidatedFields\x18\t \x03(\x0b\x32\x35.rivoli.protos.processing.Record.ValidatedFieldsEntry\x12P\n\x10\x61ggregatedFields\x18\n \x03(\x0b\x32\x36.rivoli.protos.processing.Record.AggregatedFieldsEntry\x12\x34\n\x03log\x18\x0c \x03(\x0b\x32\'.rivoli.protos.processing.ProcessingLog\x12\x43\n\x10validationErrors\x18\x0e \x03(\x0b\x32).rivoli.protos.processing.ProcessingError\x12L\n\x19validationExecutionErrors\x18\x0f \x03(\x0b\x32).rivoli.protos.processing.ProcessingError\x12>\n\x0buploadError\x18\x10 \x01(\x0b\x32).rivoli.protos.processing.ProcessingError\x12\x1c\n\x14uploadConfirmationId\x18\r \x01(\t\x1a\x33\n\x11ParsedFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14ValidatedFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15\x41ggregatedFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9a\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0e\n\nLOAD_ERROR\x10\n\x12\n\n\x06LOADED\x10\x14\x12\x0f\n\x0bPARSE_ERROR\x10\x1e\x12\n\n\x06PARSED\x10(\x12\x14\n\x10VALIDATION_ERROR\x10\x32\x12\r\n\tVALIDATED\x10<\x12\x10\n\x0cUPLOAD_ERROR\x10\x46\x12\x0c\n\x08UPLOADED\x10P\"3\n\rRecordTypeRef\x12\x16\n\x12RECORDTYPE_UNKNOWN\x10\x00\x12\n\n\x06HEADER\x10\x01\"C\n\x0fProcessingError\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x12\n\nfunctionId\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"\xe2\x02\n\x07\x43opyLog\x12\x11\n\tpartnerId\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\r\x12>\n\x05\x66iles\x18\x03 \x03(\x0b\x32/.rivoli.protos.processing.CopyLog.EvaluatedFile\x1a\xf5\x01\n\rEvaluatedFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tsizeBytes\x18\x02 \x01(\x04\x12N\n\nresolution\x18\x03 \x01(\x0e\x32:.rivoli.protos.processing.CopyLog.EvaluatedFile.Resolution\x12\x12\n\nfileTypeId\x18\x04 \x01(\t\x12\x0e\n\x06\x66ileId\x18\x05 \x01(\r\"O\n\nResolution\x12\x16\n\x12RESOLUTION_UNKNOWN\x10\x00\x12\x0c\n\x08NO_MATCH\x10\x01\x12\x0f\n\x0b\x46ILE_EXISTS\x10\x02\x12\n\n\x06\x43OPIED\x10\x03\"\xb8\x01\n\rProcessingLog\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.rivoli.protos.processing.ProcessingLog.LoggingType\x12\x0c\n\x04time\x18\x03 \x01(\r\x12\x0f\n\x07message\x18\x04 \x01(\t\"5\n\x0bLoggingType\x12\x17\n\x13LOGGINGTYPE_UNKNOWN\x10\x00\x12\r\n\tSOME_TEXT\x10\x01\"\x99\x02\n\x0bRecordTimes\x12\x18\n\x10loadingStartTime\x18\x01 \x01(\r\x12\x16\n\x0eloadingEndTime\x18\x02 \x01(\r\x12\x18\n\x10parsingStartTime\x18\x03 \x01(\r\x12\x16\n\x0eparsingEndTime\x18\x04 \x01(\r\x12\x1b\n\x13validatingStartTime\x18\x05 \x01(\r\x12\x19\n\x11validatingEndTime\x18\x06 \x01(\r\x12\x1c\n\x14\x61ggregatingStartTime\x18\x07 \x01(\r\x12\x1a\n\x12\x61ggregatingEndTime\x18\x08 \x01(\r\x12\x1a\n\x12uploadingStartTime\x18\t \x01(\r\x12\x18\n\x10uploadingEndTime\x18\n \x01(\r\"\x9c\x04\n\x0bRecordStats\x12\x17\n\x0f\x61pproximateRows\x18\x01 \x01(\r\x12\x1c\n\x14loadedRecordsSuccess\x18\x02 \x01(\r\x12\x1a\n\x12loadedRecordsError\x18\x03 \x01(\r\x12\x11\n\ttotalRows\x18\x04 \x01(\r\x12\x1c\n\x14parsedRecordsSuccess\x18\x05 \x01(\r\x12\x1a\n\x12parsedRecordsError\x18\x06 \x01(\r\x12\x1f\n\x17validatedRecordsSuccess\x18\x07 \x01(\r\x12\x1d\n\x15validatedRecordsError\x18\x08 \x01(\r\x12!\n\x19validationExecutionErrors\x18\r \x01(\r\x12\x18\n\x10validationErrors\x18\t \x01(\r\x12\x1e\n\x16uploadedRecordsSuccess\x18\x0e \x01(\r\x12\x1c\n\x14uploadedRecordsError\x18\x0f \x01(\r\x12\x1e\n\x16uploadedRecordsSkipped\x18\x10 \x01(\r\x12?\n\x05steps\x18\n \x03(\x0b\x32\x30.rivoli.protos.processing.RecordStats.StepsEntry\x1aQ\n\nStepsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.rivoli.protos.processing.StepStats:\x02\x38\x01\"<\n\tStepStats\x12\r\n\x05input\x18\x02 \x01(\r\x12\x0f\n\x07success\x18\x03 \x01(\r\x12\x0f\n\x07\x66\x61ilure\x18\x04 \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.processing_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILE_TAGSENTRY._options = None
  _FILE_TAGSENTRY._serialized_options = b'8\001'
  _RECORD_PARSEDFIELDSENTRY._options = None
  _RECORD_PARSEDFIELDSENTRY._serialized_options = b'8\001'
  _RECORD_VALIDATEDFIELDSENTRY._options = None
  _RECORD_VALIDATEDFIELDSENTRY._serialized_options = b'8\001'
  _RECORD_AGGREGATEDFIELDSENTRY._options = None
  _RECORD_AGGREGATEDFIELDSENTRY._serialized_options = b'8\001'
  _RECORDSTATS_STEPSENTRY._options = None
  _RECORDSTATS_STEPSENTRY._serialized_options = b'8\001'
  _FILE._serialized_start=54
  _FILE._serialized_end=849
  _FILE_TAGSENTRY._serialized_start=576
  _FILE_TAGSENTRY._serialized_end=619
  _FILE_STATUS._serialized_start=622
  _FILE_STATUS._serialized_end=849
  _RECORD._serialized_start=852
  _RECORD._serialized_end=1993
  _RECORD_PARSEDFIELDSENTRY._serialized_start=1619
  _RECORD_PARSEDFIELDSENTRY._serialized_end=1670
  _RECORD_VALIDATEDFIELDSENTRY._serialized_start=1672
  _RECORD_VALIDATEDFIELDSENTRY._serialized_end=1726
  _RECORD_AGGREGATEDFIELDSENTRY._serialized_start=1728
  _RECORD_AGGREGATEDFIELDSENTRY._serialized_end=1783
  _RECORD_STATUS._serialized_start=1786
  _RECORD_STATUS._serialized_end=1940
  _RECORD_RECORDTYPEREF._serialized_start=1942
  _RECORD_RECORDTYPEREF._serialized_end=1993
  _PROCESSINGERROR._serialized_start=1995
  _PROCESSINGERROR._serialized_end=2062
  _COPYLOG._serialized_start=2065
  _COPYLOG._serialized_end=2419
  _COPYLOG_EVALUATEDFILE._serialized_start=2174
  _COPYLOG_EVALUATEDFILE._serialized_end=2419
  _COPYLOG_EVALUATEDFILE_RESOLUTION._serialized_start=2340
  _COPYLOG_EVALUATEDFILE_RESOLUTION._serialized_end=2419
  _PROCESSINGLOG._serialized_start=2422
  _PROCESSINGLOG._serialized_end=2606
  _PROCESSINGLOG_LOGGINGTYPE._serialized_start=2553
  _PROCESSINGLOG_LOGGINGTYPE._serialized_end=2606
  _RECORDTIMES._serialized_start=2609
  _RECORDTIMES._serialized_end=2890
  _RECORDSTATS._serialized_start=2893
  _RECORDSTATS._serialized_end=3433
  _RECORDSTATS_STEPSENTRY._serialized_start=3352
  _RECORDSTATS_STEPSENTRY._serialized_end=3433
  _STEPSTATS._serialized_start=3435
  _STEPSTATS._serialized_end=3495
# @@protoc_insertion_point(module_scope)
