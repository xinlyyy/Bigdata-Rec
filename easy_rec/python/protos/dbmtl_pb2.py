# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_rec/python/protos/dbmtl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_rec.python.protos import dnn_pb2 as easy__rec_dot_python_dot_protos_dot_dnn__pb2
from easy_rec.python.protos import tower_pb2 as easy__rec_dot_python_dot_protos_dot_tower__pb2
from easy_rec.python.protos import cmbf_pb2 as easy__rec_dot_python_dot_protos_dot_cmbf__pb2
from easy_rec.python.protos import uniter_pb2 as easy__rec_dot_python_dot_protos_dot_uniter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_rec/python/protos/dbmtl.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n\"easy_rec/python/protos/dbmtl.proto\x12\x06protos\x1a easy_rec/python/protos/dnn.proto\x1a\"easy_rec/python/protos/tower.proto\x1a!easy_rec/python/protos/cmbf.proto\x1a#easy_rec/python/protos/uniter.proto\"\x84\x02\n\x05\x44\x42MTL\x12&\n\x0b\x62ottom_cmbf\x18\x65 \x01(\x0b\x32\x11.protos.CMBFTower\x12*\n\rbottom_uniter\x18\x66 \x01(\x0b\x32\x13.protos.UniterTower\x12\x1f\n\nbottom_dnn\x18\x01 \x01(\x0b\x32\x0b.protos.DNN\x12\x1f\n\nexpert_dnn\x18\x02 \x01(\x0b\x32\x0b.protos.DNN\x12\x15\n\nnum_expert\x18\x03 \x01(\r:\x01\x30\x12+\n\x0btask_towers\x18\x04 \x03(\x0b\x32\x16.protos.BayesTaskTower\x12!\n\x11l2_regularization\x18\x05 \x01(\x02:\x06\x30.0001')
  ,
  dependencies=[easy__rec_dot_python_dot_protos_dot_dnn__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_tower__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_cmbf__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_uniter__pb2.DESCRIPTOR,])




_DBMTL = _descriptor.Descriptor(
  name='DBMTL',
  full_name='protos.DBMTL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bottom_cmbf', full_name='protos.DBMTL.bottom_cmbf', index=0,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom_uniter', full_name='protos.DBMTL.bottom_uniter', index=1,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom_dnn', full_name='protos.DBMTL.bottom_dnn', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expert_dnn', full_name='protos.DBMTL.expert_dnn', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_expert', full_name='protos.DBMTL.num_expert', index=4,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_towers', full_name='protos.DBMTL.task_towers', index=5,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='l2_regularization', full_name='protos.DBMTL.l2_regularization', index=6,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.0001),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=449,
)

_DBMTL.fields_by_name['bottom_cmbf'].message_type = easy__rec_dot_python_dot_protos_dot_cmbf__pb2._CMBFTOWER
_DBMTL.fields_by_name['bottom_uniter'].message_type = easy__rec_dot_python_dot_protos_dot_uniter__pb2._UNITERTOWER
_DBMTL.fields_by_name['bottom_dnn'].message_type = easy__rec_dot_python_dot_protos_dot_dnn__pb2._DNN
_DBMTL.fields_by_name['expert_dnn'].message_type = easy__rec_dot_python_dot_protos_dot_dnn__pb2._DNN
_DBMTL.fields_by_name['task_towers'].message_type = easy__rec_dot_python_dot_protos_dot_tower__pb2._BAYESTASKTOWER
DESCRIPTOR.message_types_by_name['DBMTL'] = _DBMTL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DBMTL = _reflection.GeneratedProtocolMessageType('DBMTL', (_message.Message,), dict(
  DESCRIPTOR = _DBMTL,
  __module__ = 'easy_rec.python.protos.dbmtl_pb2'
  # @@protoc_insertion_point(class_scope:protos.DBMTL)
  ))
_sym_db.RegisterMessage(DBMTL)


# @@protoc_insertion_point(module_scope)
