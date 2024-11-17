# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_rec/python/protos/seq_encoder.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_rec/python/protos/seq_encoder.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n(easy_rec/python/protos/seq_encoder.proto\x12\x06protos\x1a easy_rec/python/protos/dnn.proto\"\xc5\x01\n\tAttention\x12\x18\n\tuse_scale\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cscale_by_dim\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x17\n\nscore_mode\x18\x03 \x01(\t:\x03\x64ot\x12\x12\n\x07\x64ropout\x18\x04 \x01(\x02:\x01\x30\x12\x0c\n\x04seed\x18\x05 \x01(\x05\x12&\n\x17return_attention_scores\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fuse_causal_mask\x18\x07 \x01(\x08:\x05\x66\x61lse\"\xba\x02\n\x12MultiHeadAttention\x12\x11\n\tnum_heads\x18\x01 \x02(\r\x12\x0f\n\x07key_dim\x18\x02 \x02(\r\x12\x11\n\tvalue_dim\x18\x03 \x01(\r\x12\x12\n\x07\x64ropout\x18\x04 \x01(\x02:\x01\x30\x12\x16\n\x08use_bias\x18\x05 \x01(\x08:\x04true\x12&\n\x17return_attention_scores\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fuse_causal_mask\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0coutput_shape\x18\x08 \x01(\r\x12\x16\n\x0e\x61ttention_axes\x18\t \x03(\x05\x12*\n\x12kernel_initializer\x18\n \x01(\t:\x0eglorot_uniform\x12\x1f\n\x10\x62ias_initializer\x18\x0b \x01(\t:\x05zeros\"\xe7\x02\n\x0bTransformer\x12\x13\n\x0bhidden_size\x18\x01 \x02(\r\x12\x19\n\x11num_hidden_layers\x18\x02 \x02(\r\x12\x1b\n\x13num_attention_heads\x18\x03 \x02(\r\x12\x19\n\x11intermediate_size\x18\x04 \x02(\r\x12\x18\n\nhidden_act\x18\x05 \x02(\t:\x04relu\x12 \n\x13hidden_dropout_prob\x18\x06 \x02(\x02:\x03\x30.1\x12\x12\n\nvocab_size\x18\x07 \x02(\r\x12$\n\x17max_position_embeddings\x18\x08 \x02(\r:\x03\x35\x31\x32\x12&\n\x17use_position_embeddings\x18\t \x02(\x08:\x05\x66\x61lse\x12)\n\x1boutput_all_token_embeddings\x18\n \x02(\x08:\x04true\x12\'\n\x1c\x61ttention_probs_dropout_prob\x18\x0b \x01(\x02:\x01\x30\"~\n\x0bTextEncoder\x12(\n\x0btransformer\x18\x01 \x02(\x0b\x32\x13.protos.Transformer\x12\x14\n\tseparator\x18\x02 \x02(\t:\x01 \x12\x12\n\nvocab_file\x18\x03 \x01(\t\x12\x1b\n\x10\x64\x65\x66\x61ult_token_id\x18\x04 \x01(\x05:\x01\x30\"\xbf\x03\n\nBSTEncoder\x12\x13\n\x0bhidden_size\x18\x01 \x02(\r\x12\x19\n\x11num_hidden_layers\x18\x02 \x02(\r\x12\x1b\n\x13num_attention_heads\x18\x03 \x02(\r\x12\x19\n\x11intermediate_size\x18\x04 \x02(\r\x12\x18\n\nhidden_act\x18\x05 \x02(\t:\x04gelu\x12 \n\x13hidden_dropout_prob\x18\x06 \x02(\x02:\x03\x30.1\x12)\n\x1c\x61ttention_probs_dropout_prob\x18\x07 \x02(\x02:\x03\x30.1\x12$\n\x17max_position_embeddings\x18\x08 \x02(\r:\x03\x35\x31\x32\x12%\n\x17use_position_embeddings\x18\t \x02(\x08:\x04true\x12\x1f\n\x11initializer_range\x18\n \x02(\x02:\x04\x30.02\x12)\n\x1boutput_all_token_embeddings\x18\x0b \x02(\x08:\x04true\x12\"\n\x14target_item_position\x18\x0c \x02(\t:\x04head\x12%\n\x17reserve_target_position\x18\r \x02(\x08:\x04true\"z\n\nDINEncoder\x12\"\n\rattention_dnn\x18\x01 \x02(\x0b\x32\x0b.protos.MLP\x12!\n\x13need_target_feature\x18\x02 \x02(\x08:\x04true\x12%\n\x14\x61ttention_normalizer\x18\x03 \x02(\t:\x07softmax\"\\\n\x0fSequenceAugment\x12\x16\n\tmask_rate\x18\x01 \x02(\x02:\x03\x30.6\x12\x16\n\tcrop_rate\x18\x02 \x02(\x02:\x03\x30.2\x12\x19\n\x0creorder_rate\x18\x03 \x02(\x02:\x03\x30.6')
  ,
  dependencies=[easy__rec_dot_python_dot_protos_dot_dnn__pb2.DESCRIPTOR,])




_ATTENTION = _descriptor.Descriptor(
  name='Attention',
  full_name='protos.Attention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_scale', full_name='protos.Attention.use_scale', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale_by_dim', full_name='protos.Attention.scale_by_dim', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_mode', full_name='protos.Attention.score_mode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("dot").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout', full_name='protos.Attention.dropout', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='protos.Attention.seed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_attention_scores', full_name='protos.Attention.return_attention_scores', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_causal_mask', full_name='protos.Attention.use_causal_mask', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=87,
  serialized_end=284,
)


_MULTIHEADATTENTION = _descriptor.Descriptor(
  name='MultiHeadAttention',
  full_name='protos.MultiHeadAttention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_heads', full_name='protos.MultiHeadAttention.num_heads', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_dim', full_name='protos.MultiHeadAttention.key_dim', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_dim', full_name='protos.MultiHeadAttention.value_dim', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout', full_name='protos.MultiHeadAttention.dropout', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_bias', full_name='protos.MultiHeadAttention.use_bias', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_attention_scores', full_name='protos.MultiHeadAttention.return_attention_scores', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_causal_mask', full_name='protos.MultiHeadAttention.use_causal_mask', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_shape', full_name='protos.MultiHeadAttention.output_shape', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention_axes', full_name='protos.MultiHeadAttention.attention_axes', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_initializer', full_name='protos.MultiHeadAttention.kernel_initializer', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("glorot_uniform").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bias_initializer', full_name='protos.MultiHeadAttention.bias_initializer', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("zeros").decode('utf-8'),
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
  serialized_start=287,
  serialized_end=601,
)


_TRANSFORMER = _descriptor.Descriptor(
  name='Transformer',
  full_name='protos.Transformer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hidden_size', full_name='protos.Transformer.hidden_size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_hidden_layers', full_name='protos.Transformer.num_hidden_layers', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_attention_heads', full_name='protos.Transformer.num_attention_heads', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intermediate_size', full_name='protos.Transformer.intermediate_size', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden_act', full_name='protos.Transformer.hidden_act', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("relu").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden_dropout_prob', full_name='protos.Transformer.hidden_dropout_prob', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocab_size', full_name='protos.Transformer.vocab_size', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_position_embeddings', full_name='protos.Transformer.max_position_embeddings', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_position_embeddings', full_name='protos.Transformer.use_position_embeddings', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_all_token_embeddings', full_name='protos.Transformer.output_all_token_embeddings', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention_probs_dropout_prob', full_name='protos.Transformer.attention_probs_dropout_prob', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=604,
  serialized_end=963,
)


_TEXTENCODER = _descriptor.Descriptor(
  name='TextEncoder',
  full_name='protos.TextEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformer', full_name='protos.TextEncoder.transformer', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator', full_name='protos.TextEncoder.separator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b(" ").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocab_file', full_name='protos.TextEncoder.vocab_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_token_id', full_name='protos.TextEncoder.default_token_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=965,
  serialized_end=1091,
)


_BSTENCODER = _descriptor.Descriptor(
  name='BSTEncoder',
  full_name='protos.BSTEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hidden_size', full_name='protos.BSTEncoder.hidden_size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_hidden_layers', full_name='protos.BSTEncoder.num_hidden_layers', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_attention_heads', full_name='protos.BSTEncoder.num_attention_heads', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intermediate_size', full_name='protos.BSTEncoder.intermediate_size', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden_act', full_name='protos.BSTEncoder.hidden_act', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("gelu").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden_dropout_prob', full_name='protos.BSTEncoder.hidden_dropout_prob', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention_probs_dropout_prob', full_name='protos.BSTEncoder.attention_probs_dropout_prob', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_position_embeddings', full_name='protos.BSTEncoder.max_position_embeddings', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_position_embeddings', full_name='protos.BSTEncoder.use_position_embeddings', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initializer_range', full_name='protos.BSTEncoder.initializer_range', index=9,
      number=10, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.02),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_all_token_embeddings', full_name='protos.BSTEncoder.output_all_token_embeddings', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_item_position', full_name='protos.BSTEncoder.target_item_position', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("head").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reserve_target_position', full_name='protos.BSTEncoder.reserve_target_position', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
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
  serialized_start=1094,
  serialized_end=1541,
)


_DINENCODER = _descriptor.Descriptor(
  name='DINEncoder',
  full_name='protos.DINEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attention_dnn', full_name='protos.DINEncoder.attention_dnn', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='need_target_feature', full_name='protos.DINEncoder.need_target_feature', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention_normalizer', full_name='protos.DINEncoder.attention_normalizer', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("softmax").decode('utf-8'),
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
  serialized_start=1543,
  serialized_end=1665,
)


_SEQUENCEAUGMENT = _descriptor.Descriptor(
  name='SequenceAugment',
  full_name='protos.SequenceAugment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mask_rate', full_name='protos.SequenceAugment.mask_rate', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.6),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_rate', full_name='protos.SequenceAugment.crop_rate', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reorder_rate', full_name='protos.SequenceAugment.reorder_rate', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.6),
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
  serialized_start=1667,
  serialized_end=1759,
)

_TEXTENCODER.fields_by_name['transformer'].message_type = _TRANSFORMER
_DINENCODER.fields_by_name['attention_dnn'].message_type = easy__rec_dot_python_dot_protos_dot_dnn__pb2._MLP
DESCRIPTOR.message_types_by_name['Attention'] = _ATTENTION
DESCRIPTOR.message_types_by_name['MultiHeadAttention'] = _MULTIHEADATTENTION
DESCRIPTOR.message_types_by_name['Transformer'] = _TRANSFORMER
DESCRIPTOR.message_types_by_name['TextEncoder'] = _TEXTENCODER
DESCRIPTOR.message_types_by_name['BSTEncoder'] = _BSTENCODER
DESCRIPTOR.message_types_by_name['DINEncoder'] = _DINENCODER
DESCRIPTOR.message_types_by_name['SequenceAugment'] = _SEQUENCEAUGMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attention = _reflection.GeneratedProtocolMessageType('Attention', (_message.Message,), dict(
  DESCRIPTOR = _ATTENTION,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.Attention)
  ))
_sym_db.RegisterMessage(Attention)

MultiHeadAttention = _reflection.GeneratedProtocolMessageType('MultiHeadAttention', (_message.Message,), dict(
  DESCRIPTOR = _MULTIHEADATTENTION,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.MultiHeadAttention)
  ))
_sym_db.RegisterMessage(MultiHeadAttention)

Transformer = _reflection.GeneratedProtocolMessageType('Transformer', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMER,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.Transformer)
  ))
_sym_db.RegisterMessage(Transformer)

TextEncoder = _reflection.GeneratedProtocolMessageType('TextEncoder', (_message.Message,), dict(
  DESCRIPTOR = _TEXTENCODER,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.TextEncoder)
  ))
_sym_db.RegisterMessage(TextEncoder)

BSTEncoder = _reflection.GeneratedProtocolMessageType('BSTEncoder', (_message.Message,), dict(
  DESCRIPTOR = _BSTENCODER,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.BSTEncoder)
  ))
_sym_db.RegisterMessage(BSTEncoder)

DINEncoder = _reflection.GeneratedProtocolMessageType('DINEncoder', (_message.Message,), dict(
  DESCRIPTOR = _DINENCODER,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.DINEncoder)
  ))
_sym_db.RegisterMessage(DINEncoder)

SequenceAugment = _reflection.GeneratedProtocolMessageType('SequenceAugment', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCEAUGMENT,
  __module__ = 'easy_rec.python.protos.seq_encoder_pb2'
  # @@protoc_insertion_point(class_scope:protos.SequenceAugment)
  ))
_sym_db.RegisterMessage(SequenceAugment)


# @@protoc_insertion_point(module_scope)
