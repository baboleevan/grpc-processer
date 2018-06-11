# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: processer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='processer.proto',
  package='grpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0fprocesser.proto\x12\x04grpc\"4\n\x0cInputRequest\x12\r\n\x05input\x18\x01 \x01(\t\x12\x15\n\routputs_count\x18\x02 \x01(\x05\"9\n\rReloadRequest\x12\x0c\n\x04\x63mds\x18\x01 \x03(\t\x12\x1a\n\x12header_lines_count\x18\x02 \x01(\x05\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eOutputResponse\x12\x0f\n\x07results\x18\x01 \x01(\t2q\n\tProcesser\x12\x33\n\x05Input\x12\x12.grpc.InputRequest\x1a\x14.grpc.OutputResponse\"\x00\x12/\n\x06Reload\x12\x13.grpc.ReloadRequest\x1a\x0e.grpc.Response\"\x00\x62\x06proto3')
)




_INPUTREQUEST = _descriptor.Descriptor(
  name='InputRequest',
  full_name='grpc.InputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='grpc.InputRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs_count', full_name='grpc.InputRequest.outputs_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=77,
)


_RELOADREQUEST = _descriptor.Descriptor(
  name='ReloadRequest',
  full_name='grpc.ReloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmds', full_name='grpc.ReloadRequest.cmds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_lines_count', full_name='grpc.ReloadRequest.header_lines_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=136,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='grpc.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=165,
)


_OUTPUTRESPONSE = _descriptor.Descriptor(
  name='OutputResponse',
  full_name='grpc.OutputResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='grpc.OutputResponse.results', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['InputRequest'] = _INPUTREQUEST
DESCRIPTOR.message_types_by_name['ReloadRequest'] = _RELOADREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['OutputResponse'] = _OUTPUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputRequest = _reflection.GeneratedProtocolMessageType('InputRequest', (_message.Message,), dict(
  DESCRIPTOR = _INPUTREQUEST,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.InputRequest)
  ))
_sym_db.RegisterMessage(InputRequest)

ReloadRequest = _reflection.GeneratedProtocolMessageType('ReloadRequest', (_message.Message,), dict(
  DESCRIPTOR = _RELOADREQUEST,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ReloadRequest)
  ))
_sym_db.RegisterMessage(ReloadRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Response)
  ))
_sym_db.RegisterMessage(Response)

OutputResponse = _reflection.GeneratedProtocolMessageType('OutputResponse', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTRESPONSE,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.OutputResponse)
  ))
_sym_db.RegisterMessage(OutputResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class ProcesserStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Input = channel.unary_unary(
          '/grpc.Processer/Input',
          request_serializer=InputRequest.SerializeToString,
          response_deserializer=OutputResponse.FromString,
          )
      self.Reload = channel.unary_unary(
          '/grpc.Processer/Reload',
          request_serializer=ReloadRequest.SerializeToString,
          response_deserializer=Response.FromString,
          )


  class ProcesserServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Input(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Reload(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ProcesserServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Input': grpc.unary_unary_rpc_method_handler(
            servicer.Input,
            request_deserializer=InputRequest.FromString,
            response_serializer=OutputResponse.SerializeToString,
        ),
        'Reload': grpc.unary_unary_rpc_method_handler(
            servicer.Reload,
            request_deserializer=ReloadRequest.FromString,
            response_serializer=Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc.Processer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaProcesserServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Input(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Reload(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaProcesserStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Input(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Input.future = None
    def Reload(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Reload.future = None


  def beta_create_Processer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('grpc.Processer', 'Input'): InputRequest.FromString,
      ('grpc.Processer', 'Reload'): ReloadRequest.FromString,
    }
    response_serializers = {
      ('grpc.Processer', 'Input'): OutputResponse.SerializeToString,
      ('grpc.Processer', 'Reload'): Response.SerializeToString,
    }
    method_implementations = {
      ('grpc.Processer', 'Input'): face_utilities.unary_unary_inline(servicer.Input),
      ('grpc.Processer', 'Reload'): face_utilities.unary_unary_inline(servicer.Reload),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Processer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('grpc.Processer', 'Input'): InputRequest.SerializeToString,
      ('grpc.Processer', 'Reload'): ReloadRequest.SerializeToString,
    }
    response_deserializers = {
      ('grpc.Processer', 'Input'): OutputResponse.FromString,
      ('grpc.Processer', 'Reload'): Response.FromString,
    }
    cardinalities = {
      'Input': cardinality.Cardinality.UNARY_UNARY,
      'Reload': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'grpc.Processer', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
