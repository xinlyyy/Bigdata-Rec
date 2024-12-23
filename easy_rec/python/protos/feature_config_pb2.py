# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_rec/python/protos/feature_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_rec.python.protos import hyperparams_pb2 as easy__rec_dot_python_dot_protos_dot_hyperparams__pb2
from easy_rec.python.protos import dnn_pb2 as easy__rec_dot_python_dot_protos_dot_dnn__pb2
from easy_rec.python.protos import layer_pb2 as easy__rec_dot_python_dot_protos_dot_layer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_rec/python/protos/feature_config.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n+easy_rec/python/protos/feature_config.proto\x12\x06protos\x1a(easy_rec/python/protos/hyperparams.proto\x1a easy_rec/python/protos/dnn.proto\x1a\"easy_rec/python/protos/layer.proto\"\x13\n\x11\x41ttentionCombiner\"\x1c\n\x1aMultiHeadAttentionCombiner\"\xb7\x01\n\x10SequenceCombiner\x12.\n\tattention\x18\x01 \x01(\x0b\x32\x19.protos.AttentionCombinerH\x00\x12\x42\n\x14multi_head_attention\x18\x02 \x01(\x0b\x32\".protos.MultiHeadAttentionCombinerH\x00\x12#\n\x08text_cnn\x18\x03 \x01(\x0b\x32\x0f.protos.TextCNNH\x00\x42\n\n\x08\x63ombiner\"\x96\x01\n\x08\x45VParams\x12\x16\n\x0b\x66ilter_freq\x18\x01 \x01(\x04:\x01\x30\x12\x18\n\rsteps_to_live\x18\x02 \x01(\x04:\x01\x30\x12\x18\n\tuse_cache\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\rinit_capacity\x18\x04 \x01(\x04:\x07\x38\x33\x38\x38\x36\x30\x38\x12\x1e\n\x0cmax_capacity\x18\x05 \x01(\x04:\x08\x31\x36\x37\x37\x37\x32\x31\x36\"\xff\x08\n\rFeatureConfig\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x13\n\x0binput_names\x18\x02 \x03(\t\x12\x42\n\x0c\x66\x65\x61ture_type\x18\x03 \x02(\x0e\x32!.protos.FeatureConfig.FeatureType:\tIdFeature\x12\x18\n\x0e\x65mbedding_name\x18\x04 \x01(\t:\x00\x12\x18\n\rembedding_dim\x18\x05 \x01(\r:\x01\x30\x12\x1b\n\x10hash_bucket_size\x18\x06 \x01(\x04:\x01\x30\x12\x16\n\x0bnum_buckets\x18\x07 \x01(\x04:\x01\x30\x12\x12\n\nboundaries\x18\x08 \x03(\x01\x12\x14\n\tseparator\x18\t \x01(\t:\x01|\x12\x14\n\x0ckv_separator\x18\n \x01(\t\x12\x15\n\rseq_multi_sep\x18\x65 \x01(\t\x12\x13\n\x0bmax_seq_len\x18\x66 \x01(\r\x12\x12\n\nvocab_file\x18\x0b \x01(\t\x12\x12\n\nvocab_list\x18\x0c \x03(\t\x12\x14\n\x0cshared_names\x18\x10 \x03(\t\x12#\n\x17lookup_max_sel_elem_num\x18\x11 \x01(\x05:\x02\x31\x30\x12\x19\n\x0emax_partitions\x18\x12 \x01(\x05:\x01\x31\x12\x15\n\x08\x63ombiner\x18\x13 \x01(\t:\x03sum\x12(\n\x0binitializer\x18\x14 \x01(\x0b\x32\x13.protos.Initializer\x12\x15\n\tprecision\x18\x15 \x01(\x05:\x02-1\x12\x13\n\x07min_val\x18\xd4\x01 \x01(\x01:\x01\x30\x12\x13\n\x07max_val\x18\xd5\x01 \x01(\x01:\x01\x30\x12\x16\n\rnormalizer_fn\x18\xd6\x01 \x01(\t\x12\x18\n\rraw_input_dim\x18\x18 \x01(\r:\x01\x31\x12\x33\n\x11sequence_combiner\x18\x19 \x01(\x0b\x32\x18.protos.SequenceCombiner\x12\x46\n\x10sub_feature_type\x18\x1a \x01(\x0e\x32!.protos.FeatureConfig.FeatureType:\tIdFeature\x12\x1a\n\x0fsequence_length\x18\x1b \x01(\r:\x01\x31\x12\x12\n\nexpression\x18\x1e \x01(\t\x12#\n\tev_params\x18\x1f \x01(\x0b\x32\x10.protos.EVParams\x12\x19\n\x0e\x63ombo_join_sep\x18\x91\x03 \x01(\t:\x00\x12\x19\n\x10\x63ombo_input_seps\x18\x92\x03 \x03(\t\"\x9f\x01\n\x0b\x46\x65\x61tureType\x12\r\n\tIdFeature\x10\x00\x12\x0e\n\nRawFeature\x10\x01\x12\x0e\n\nTagFeature\x10\x02\x12\x10\n\x0c\x43omboFeature\x10\x03\x12\x11\n\rLookupFeature\x10\x04\x12\x13\n\x0fSequenceFeature\x10\x05\x12\x0f\n\x0b\x45xprFeature\x10\x06\x12\x16\n\x12PassThroughFeature\x10\x07\"N\n\tFieldType\x12\t\n\x05INT32\x10\x00\x12\t\n\x05INT64\x10\x01\x12\n\n\x06STRING\x10\x02\x12\t\n\x05\x46LOAT\x10\x04\x12\n\n\x06\x44OUBLE\x10\x05\x12\x08\n\x04\x42OOL\x10\x06\"[\n\x0f\x46\x65\x61tureConfigV2\x12\'\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x15.protos.FeatureConfig\x12\x1f\n\x10\x65mbedding_on_cpu\x18\x02 \x01(\x08:\x05\x66\x61lse\"\xc3\x01\n\x12\x46\x65\x61tureGroupConfig\x12\x12\n\ngroup_name\x18\x01 \x01(\t\x12\x15\n\rfeature_names\x18\x02 \x03(\t\x12+\n\twide_deep\x18\x03 \x01(\x0e\x32\x12.protos.WideOrDeep:\x04\x44\x45\x45P\x12\x34\n\x11sequence_features\x18\x04 \x03(\x0b\x32\x19.protos.SeqAttGroupConfig\x12\x1f\n\x10negative_sampler\x18\x05 \x01(\x08:\x05\x66\x61lse\"@\n\tSeqAttMap\x12\x0b\n\x03key\x18\x01 \x03(\t\x12\x10\n\x08hist_seq\x18\x02 \x03(\t\x12\x14\n\x0c\x61ux_hist_seq\x18\x03 \x03(\t\"\x8b\x02\n\x11SeqAttGroupConfig\x12\x12\n\ngroup_name\x18\x01 \x01(\t\x12&\n\x0bseq_att_map\x18\x02 \x03(\x0b\x32\x11.protos.SeqAttMap\x12\x19\n\ntf_summary\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x07seq_dnn\x18\x04 \x01(\x0b\x32\x0b.protos.DNN\x12\x1f\n\x10\x61llow_key_search\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x10need_key_feature\x18\x06 \x01(\x08:\x04true\x12\"\n\x13\x61llow_key_transform\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rtransform_dnn\x18\x08 \x01(\x08:\x05\x66\x61lse*3\n\nWideOrDeep\x12\x08\n\x04\x44\x45\x45P\x10\x00\x12\x08\n\x04WIDE\x10\x01\x12\x11\n\rWIDE_AND_DEEP\x10\x02')
  ,
  dependencies=[easy__rec_dot_python_dot_protos_dot_hyperparams__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_dnn__pb2.DESCRIPTOR,easy__rec_dot_python_dot_protos_dot_layer__pb2.DESCRIPTOR,])

_WIDEORDEEP = _descriptor.EnumDescriptor(
  name='WideOrDeep',
  full_name='protos.WideOrDeep',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEEP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIDE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIDE_AND_DEEP', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2338,
  serialized_end=2389,
)
_sym_db.RegisterEnumDescriptor(_WIDEORDEEP)

WideOrDeep = enum_type_wrapper.EnumTypeWrapper(_WIDEORDEEP)
DEEP = 0
WIDE = 1
WIDE_AND_DEEP = 2


_FEATURECONFIG_FEATURETYPE = _descriptor.EnumDescriptor(
  name='FeatureType',
  full_name='protos.FeatureConfig.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IdFeature', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RawFeature', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TagFeature', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ComboFeature', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LookupFeature', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SequenceFeature', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ExprFeature', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PassThroughFeature', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1470,
  serialized_end=1629,
)
_sym_db.RegisterEnumDescriptor(_FEATURECONFIG_FEATURETYPE)

_FEATURECONFIG_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='protos.FeatureConfig.FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT32', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1631,
  serialized_end=1709,
)
_sym_db.RegisterEnumDescriptor(_FEATURECONFIG_FIELDTYPE)


_ATTENTIONCOMBINER = _descriptor.Descriptor(
  name='AttentionCombiner',
  full_name='protos.AttentionCombiner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=167,
  serialized_end=186,
)


_MULTIHEADATTENTIONCOMBINER = _descriptor.Descriptor(
  name='MultiHeadAttentionCombiner',
  full_name='protos.MultiHeadAttentionCombiner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=188,
  serialized_end=216,
)


_SEQUENCECOMBINER = _descriptor.Descriptor(
  name='SequenceCombiner',
  full_name='protos.SequenceCombiner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attention', full_name='protos.SequenceCombiner.attention', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_head_attention', full_name='protos.SequenceCombiner.multi_head_attention', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text_cnn', full_name='protos.SequenceCombiner.text_cnn', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='combiner', full_name='protos.SequenceCombiner.combiner',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=219,
  serialized_end=402,
)


_EVPARAMS = _descriptor.Descriptor(
  name='EVParams',
  full_name='protos.EVParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_freq', full_name='protos.EVParams.filter_freq', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps_to_live', full_name='protos.EVParams.steps_to_live', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_cache', full_name='protos.EVParams.use_cache', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_capacity', full_name='protos.EVParams.init_capacity', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=8388608,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_capacity', full_name='protos.EVParams.max_capacity', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=16777216,
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
  serialized_start=405,
  serialized_end=555,
)


_FEATURECONFIG = _descriptor.Descriptor(
  name='FeatureConfig',
  full_name='protos.FeatureConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='protos.FeatureConfig.feature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_names', full_name='protos.FeatureConfig.input_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='protos.FeatureConfig.feature_type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedding_name', full_name='protos.FeatureConfig.embedding_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedding_dim', full_name='protos.FeatureConfig.embedding_dim', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash_bucket_size', full_name='protos.FeatureConfig.hash_bucket_size', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_buckets', full_name='protos.FeatureConfig.num_buckets', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boundaries', full_name='protos.FeatureConfig.boundaries', index=7,
      number=8, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator', full_name='protos.FeatureConfig.separator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("|").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kv_separator', full_name='protos.FeatureConfig.kv_separator', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq_multi_sep', full_name='protos.FeatureConfig.seq_multi_sep', index=10,
      number=101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_seq_len', full_name='protos.FeatureConfig.max_seq_len', index=11,
      number=102, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocab_file', full_name='protos.FeatureConfig.vocab_file', index=12,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocab_list', full_name='protos.FeatureConfig.vocab_list', index=13,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shared_names', full_name='protos.FeatureConfig.shared_names', index=14,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lookup_max_sel_elem_num', full_name='protos.FeatureConfig.lookup_max_sel_elem_num', index=15,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_partitions', full_name='protos.FeatureConfig.max_partitions', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combiner', full_name='protos.FeatureConfig.combiner', index=17,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("sum").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initializer', full_name='protos.FeatureConfig.initializer', index=18,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='protos.FeatureConfig.precision', index=19,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_val', full_name='protos.FeatureConfig.min_val', index=20,
      number=212, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_val', full_name='protos.FeatureConfig.max_val', index=21,
      number=213, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalizer_fn', full_name='protos.FeatureConfig.normalizer_fn', index=22,
      number=214, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_input_dim', full_name='protos.FeatureConfig.raw_input_dim', index=23,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_combiner', full_name='protos.FeatureConfig.sequence_combiner', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_feature_type', full_name='protos.FeatureConfig.sub_feature_type', index=25,
      number=26, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_length', full_name='protos.FeatureConfig.sequence_length', index=26,
      number=27, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expression', full_name='protos.FeatureConfig.expression', index=27,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ev_params', full_name='protos.FeatureConfig.ev_params', index=28,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combo_join_sep', full_name='protos.FeatureConfig.combo_join_sep', index=29,
      number=401, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combo_input_seps', full_name='protos.FeatureConfig.combo_input_seps', index=30,
      number=402, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATURECONFIG_FEATURETYPE,
    _FEATURECONFIG_FIELDTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=1709,
)


_FEATURECONFIGV2 = _descriptor.Descriptor(
  name='FeatureConfigV2',
  full_name='protos.FeatureConfigV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='protos.FeatureConfigV2.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedding_on_cpu', full_name='protos.FeatureConfigV2.embedding_on_cpu', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=1711,
  serialized_end=1802,
)


_FEATUREGROUPCONFIG = _descriptor.Descriptor(
  name='FeatureGroupConfig',
  full_name='protos.FeatureGroupConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_name', full_name='protos.FeatureGroupConfig.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_names', full_name='protos.FeatureGroupConfig.feature_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wide_deep', full_name='protos.FeatureGroupConfig.wide_deep', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_features', full_name='protos.FeatureGroupConfig.sequence_features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negative_sampler', full_name='protos.FeatureGroupConfig.negative_sampler', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=1805,
  serialized_end=2000,
)


_SEQATTMAP = _descriptor.Descriptor(
  name='SeqAttMap',
  full_name='protos.SeqAttMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.SeqAttMap.key', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hist_seq', full_name='protos.SeqAttMap.hist_seq', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux_hist_seq', full_name='protos.SeqAttMap.aux_hist_seq', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=2002,
  serialized_end=2066,
)


_SEQATTGROUPCONFIG = _descriptor.Descriptor(
  name='SeqAttGroupConfig',
  full_name='protos.SeqAttGroupConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_name', full_name='protos.SeqAttGroupConfig.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq_att_map', full_name='protos.SeqAttGroupConfig.seq_att_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tf_summary', full_name='protos.SeqAttGroupConfig.tf_summary', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq_dnn', full_name='protos.SeqAttGroupConfig.seq_dnn', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_key_search', full_name='protos.SeqAttGroupConfig.allow_key_search', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='need_key_feature', full_name='protos.SeqAttGroupConfig.need_key_feature', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_key_transform', full_name='protos.SeqAttGroupConfig.allow_key_transform', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform_dnn', full_name='protos.SeqAttGroupConfig.transform_dnn', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=2069,
  serialized_end=2336,
)

_SEQUENCECOMBINER.fields_by_name['attention'].message_type = _ATTENTIONCOMBINER
_SEQUENCECOMBINER.fields_by_name['multi_head_attention'].message_type = _MULTIHEADATTENTIONCOMBINER
_SEQUENCECOMBINER.fields_by_name['text_cnn'].message_type = easy__rec_dot_python_dot_protos_dot_layer__pb2._TEXTCNN
_SEQUENCECOMBINER.oneofs_by_name['combiner'].fields.append(
  _SEQUENCECOMBINER.fields_by_name['attention'])
_SEQUENCECOMBINER.fields_by_name['attention'].containing_oneof = _SEQUENCECOMBINER.oneofs_by_name['combiner']
_SEQUENCECOMBINER.oneofs_by_name['combiner'].fields.append(
  _SEQUENCECOMBINER.fields_by_name['multi_head_attention'])
_SEQUENCECOMBINER.fields_by_name['multi_head_attention'].containing_oneof = _SEQUENCECOMBINER.oneofs_by_name['combiner']
_SEQUENCECOMBINER.oneofs_by_name['combiner'].fields.append(
  _SEQUENCECOMBINER.fields_by_name['text_cnn'])
_SEQUENCECOMBINER.fields_by_name['text_cnn'].containing_oneof = _SEQUENCECOMBINER.oneofs_by_name['combiner']
_FEATURECONFIG.fields_by_name['feature_type'].enum_type = _FEATURECONFIG_FEATURETYPE
_FEATURECONFIG.fields_by_name['initializer'].message_type = easy__rec_dot_python_dot_protos_dot_hyperparams__pb2._INITIALIZER
_FEATURECONFIG.fields_by_name['sequence_combiner'].message_type = _SEQUENCECOMBINER
_FEATURECONFIG.fields_by_name['sub_feature_type'].enum_type = _FEATURECONFIG_FEATURETYPE
_FEATURECONFIG.fields_by_name['ev_params'].message_type = _EVPARAMS
_FEATURECONFIG_FEATURETYPE.containing_type = _FEATURECONFIG
_FEATURECONFIG_FIELDTYPE.containing_type = _FEATURECONFIG
_FEATURECONFIGV2.fields_by_name['features'].message_type = _FEATURECONFIG
_FEATUREGROUPCONFIG.fields_by_name['wide_deep'].enum_type = _WIDEORDEEP
_FEATUREGROUPCONFIG.fields_by_name['sequence_features'].message_type = _SEQATTGROUPCONFIG
_SEQATTGROUPCONFIG.fields_by_name['seq_att_map'].message_type = _SEQATTMAP
_SEQATTGROUPCONFIG.fields_by_name['seq_dnn'].message_type = easy__rec_dot_python_dot_protos_dot_dnn__pb2._DNN
DESCRIPTOR.message_types_by_name['AttentionCombiner'] = _ATTENTIONCOMBINER
DESCRIPTOR.message_types_by_name['MultiHeadAttentionCombiner'] = _MULTIHEADATTENTIONCOMBINER
DESCRIPTOR.message_types_by_name['SequenceCombiner'] = _SEQUENCECOMBINER
DESCRIPTOR.message_types_by_name['EVParams'] = _EVPARAMS
DESCRIPTOR.message_types_by_name['FeatureConfig'] = _FEATURECONFIG
DESCRIPTOR.message_types_by_name['FeatureConfigV2'] = _FEATURECONFIGV2
DESCRIPTOR.message_types_by_name['FeatureGroupConfig'] = _FEATUREGROUPCONFIG
DESCRIPTOR.message_types_by_name['SeqAttMap'] = _SEQATTMAP
DESCRIPTOR.message_types_by_name['SeqAttGroupConfig'] = _SEQATTGROUPCONFIG
DESCRIPTOR.enum_types_by_name['WideOrDeep'] = _WIDEORDEEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttentionCombiner = _reflection.GeneratedProtocolMessageType('AttentionCombiner', (_message.Message,), dict(
  DESCRIPTOR = _ATTENTIONCOMBINER,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.AttentionCombiner)
  ))
_sym_db.RegisterMessage(AttentionCombiner)

MultiHeadAttentionCombiner = _reflection.GeneratedProtocolMessageType('MultiHeadAttentionCombiner', (_message.Message,), dict(
  DESCRIPTOR = _MULTIHEADATTENTIONCOMBINER,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.MultiHeadAttentionCombiner)
  ))
_sym_db.RegisterMessage(MultiHeadAttentionCombiner)

SequenceCombiner = _reflection.GeneratedProtocolMessageType('SequenceCombiner', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCECOMBINER,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.SequenceCombiner)
  ))
_sym_db.RegisterMessage(SequenceCombiner)

EVParams = _reflection.GeneratedProtocolMessageType('EVParams', (_message.Message,), dict(
  DESCRIPTOR = _EVPARAMS,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.EVParams)
  ))
_sym_db.RegisterMessage(EVParams)

FeatureConfig = _reflection.GeneratedProtocolMessageType('FeatureConfig', (_message.Message,), dict(
  DESCRIPTOR = _FEATURECONFIG,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.FeatureConfig)
  ))
_sym_db.RegisterMessage(FeatureConfig)

FeatureConfigV2 = _reflection.GeneratedProtocolMessageType('FeatureConfigV2', (_message.Message,), dict(
  DESCRIPTOR = _FEATURECONFIGV2,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.FeatureConfigV2)
  ))
_sym_db.RegisterMessage(FeatureConfigV2)

FeatureGroupConfig = _reflection.GeneratedProtocolMessageType('FeatureGroupConfig', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREGROUPCONFIG,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.FeatureGroupConfig)
  ))
_sym_db.RegisterMessage(FeatureGroupConfig)

SeqAttMap = _reflection.GeneratedProtocolMessageType('SeqAttMap', (_message.Message,), dict(
  DESCRIPTOR = _SEQATTMAP,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.SeqAttMap)
  ))
_sym_db.RegisterMessage(SeqAttMap)

SeqAttGroupConfig = _reflection.GeneratedProtocolMessageType('SeqAttGroupConfig', (_message.Message,), dict(
  DESCRIPTOR = _SEQATTGROUPCONFIG,
  __module__ = 'easy_rec.python.protos.feature_config_pb2'
  # @@protoc_insertion_point(class_scope:protos.SeqAttGroupConfig)
  ))
_sym_db.RegisterMessage(SeqAttGroupConfig)


# @@protoc_insertion_point(module_scope)
