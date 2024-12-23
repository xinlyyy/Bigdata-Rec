# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_rec/python/protos/dssm_senet.proto

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
from easy_rec.python.protos import simi_pb2 as easy__rec_dot_python_dot_protos_dot_simi__pb2
from easy_rec.python.protos import layer_pb2 as easy__rec_dot_python_dot_protos_dot_layer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_rec/python/protos/dssm_senet.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n\'easy_rec/python/protos/dssm_senet.proto\x12\x06protos\x1a easy_rec/python/protos/dnn.proto\x1a!easy_rec/python/protos/simi.proto\x1a\"easy_rec/python/protos/layer.proto\"V\n\x10\x44SSM_SENet_Tower\x12\n\n\x02id\x18\x01 \x02(\t\x12\x1c\n\x05senet\x18\x02 \x02(\x0b\x32\r.protos.SENet\x12\x18\n\x03\x64nn\x18\x03 \x02(\x0b\x32\x0b.protos.DNN\"\xa5\x02\n\nDSSM_SENet\x12,\n\nuser_tower\x18\x01 \x02(\x0b\x32\x18.protos.DSSM_SENet_Tower\x12,\n\nitem_tower\x18\x02 \x02(\x0b\x32\x18.protos.DSSM_SENet_Tower\x12!\n\x11l2_regularization\x18\x03 \x02(\x02:\x06\x30.0001\x12-\n\tsimi_func\x18\x04 \x01(\x0e\x32\x12.protos.Similarity:\x06\x43OSINE\x12\x18\n\nscale_simi\x18\x05 \x01(\x08:\x04true\x12\x0f\n\x07item_id\x18\t \x01(\t\x12&\n\x17ignore_in_batch_neg_sam\x18\n \x02(\x08:\x05\x66\x61lse\x12\x16\n\x0btemperature\x18\x0b \x01(\x02:\x01\x31')
  ,
  dependencies=[easy__rec_dot_python_dot_protos_dot_dnn__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_simi__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_layer__pb2.DESCRIPTOR,])




_DSSM_SENET_TOWER = _descriptor.Descriptor(
  name='DSSM_SENet_Tower',
  full_name='protos.DSSM_SENet_Tower',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.DSSM_SENet_Tower.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='senet', full_name='protos.DSSM_SENet_Tower.senet', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dnn', full_name='protos.DSSM_SENet_Tower.dnn', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=156,
  serialized_end=242,
)


_DSSM_SENET = _descriptor.Descriptor(
  name='DSSM_SENet',
  full_name='protos.DSSM_SENet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_tower', full_name='protos.DSSM_SENet.user_tower', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_tower', full_name='protos.DSSM_SENet.item_tower', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='l2_regularization', full_name='protos.DSSM_SENet.l2_regularization', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.0001),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simi_func', full_name='protos.DSSM_SENet.simi_func', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale_simi', full_name='protos.DSSM_SENet.scale_simi', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='protos.DSSM_SENet.item_id', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_in_batch_neg_sam', full_name='protos.DSSM_SENet.ignore_in_batch_neg_sam', index=6,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='protos.DSSM_SENet.temperature', index=7,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=245,
  serialized_end=538,
)

_DSSM_SENET_TOWER.fields_by_name['senet'].message_type = easy__rec_dot_python_dot_protos_dot_layer__pb2._SENET
_DSSM_SENET_TOWER.fields_by_name['dnn'].message_type = easy__rec_dot_python_dot_protos_dot_dnn__pb2._DNN
_DSSM_SENET.fields_by_name['user_tower'].message_type = _DSSM_SENET_TOWER
_DSSM_SENET.fields_by_name['item_tower'].message_type = _DSSM_SENET_TOWER
_DSSM_SENET.fields_by_name['simi_func'].enum_type = easy__rec_dot_python_dot_protos_dot_simi__pb2._SIMILARITY
DESCRIPTOR.message_types_by_name['DSSM_SENet_Tower'] = _DSSM_SENET_TOWER
DESCRIPTOR.message_types_by_name['DSSM_SENet'] = _DSSM_SENET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DSSM_SENet_Tower = _reflection.GeneratedProtocolMessageType('DSSM_SENet_Tower', (_message.Message,), dict(
  DESCRIPTOR = _DSSM_SENET_TOWER,
  __module__ = 'easy_rec.python.protos.dssm_senet_pb2'
  # @@protoc_insertion_point(class_scope:protos.DSSM_SENet_Tower)
  ))
_sym_db.RegisterMessage(DSSM_SENet_Tower)

DSSM_SENet = _reflection.GeneratedProtocolMessageType('DSSM_SENet', (_message.Message,), dict(
  DESCRIPTOR = _DSSM_SENET,
  __module__ = 'easy_rec.python.protos.dssm_senet_pb2'
  # @@protoc_insertion_point(class_scope:protos.DSSM_SENet)
  ))
_sym_db.RegisterMessage(DSSM_SENet)


# @@protoc_insertion_point(module_scope)
