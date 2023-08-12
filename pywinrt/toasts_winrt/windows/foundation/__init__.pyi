# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.10

import enum
import datetime
import sys
import types
import typing

import toasts_winrt.system
import toasts_winrt.windows.foundation.collections

class AsyncStatus(enum.IntEnum):
    CANCELED = 2
    COMPLETED = 1
    ERROR = 3
    STARTED = 0

class PropertyType(enum.IntEnum):
    EMPTY = 0
    UINT8 = 1
    INT16 = 2
    UINT16 = 3
    INT32 = 4
    UINT32 = 5
    INT64 = 6
    UINT64 = 7
    SINGLE = 8
    DOUBLE = 9
    CHAR16 = 10
    BOOLEAN = 11
    STRING = 12
    INSPECTABLE = 13
    DATE_TIME = 14
    TIME_SPAN = 15
    GUID = 16
    POINT = 17
    SIZE = 18
    RECT = 19
    OTHER_TYPE = 20
    UINT8_ARRAY = 1025
    INT16_ARRAY = 1026
    UINT16_ARRAY = 1027
    INT32_ARRAY = 1028
    UINT32_ARRAY = 1029
    INT64_ARRAY = 1030
    UINT64_ARRAY = 1031
    SINGLE_ARRAY = 1032
    DOUBLE_ARRAY = 1033
    CHAR16_ARRAY = 1034
    BOOLEAN_ARRAY = 1035
    STRING_ARRAY = 1036
    INSPECTABLE_ARRAY = 1037
    DATE_TIME_ARRAY = 1038
    TIME_SPAN_ARRAY = 1039
    GUID_ARRAY = 1040
    POINT_ARRAY = 1041
    SIZE_ARRAY = 1042
    RECT_ARRAY = 1043
    OTHER_TYPE_ARRAY = 1044

Self = typing.TypeVar('Self')
T = typing.TypeVar('T')
TProgress = typing.TypeVar('TProgress')
TResult = typing.TypeVar('TResult')
TSender = typing.TypeVar('TSender')

class EventRegistrationToken:
    value: toasts_winrt.system.Int64
    def __new__(cls: typing.Type[EventRegistrationToken], value: toasts_winrt.system.Int64) -> EventRegistrationToken: ...

class HResult:
    value: toasts_winrt.system.Int32
    def __new__(cls: typing.Type[HResult], value: toasts_winrt.system.Int32) -> HResult: ...

class Point:
    x: toasts_winrt.system.Single
    y: toasts_winrt.system.Single
    def __new__(cls: typing.Type[Point], x: toasts_winrt.system.Single, y: toasts_winrt.system.Single) -> Point: ...

class Rect:
    x: toasts_winrt.system.Single
    y: toasts_winrt.system.Single
    width: toasts_winrt.system.Single
    height: toasts_winrt.system.Single
    def __new__(cls: typing.Type[Rect], x: toasts_winrt.system.Single, y: toasts_winrt.system.Single, width: toasts_winrt.system.Single, height: toasts_winrt.system.Single) -> Rect: ...

class Size:
    width: toasts_winrt.system.Single
    height: toasts_winrt.system.Single
    def __new__(cls: typing.Type[Size], width: toasts_winrt.system.Single, height: toasts_winrt.system.Single) -> Size: ...

class Deferral(toasts_winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> Deferral: ...
    def __new__(cls: typing.Type[Deferral], handler: typing.Optional[DeferralCompletedHandler]) -> Deferral:...
    def close(self) -> None: ...
    def complete(self) -> None: ...

class GuidHelper(toasts_winrt.system.Object):
    empty: typing.ClassVar[toasts_winrt.system.Guid]
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> GuidHelper: ...
    @staticmethod
    def create_new_guid() -> toasts_winrt.system.Guid: ...
    @staticmethod
    def equals(target: toasts_winrt.system.Guid, value: toasts_winrt.system.Guid, /) -> toasts_winrt.system.Boolean: ...

class MemoryBuffer(toasts_winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> MemoryBuffer: ...
    def __new__(cls: typing.Type[MemoryBuffer], capacity: toasts_winrt.system.UInt32) -> MemoryBuffer:...
    def close(self) -> None: ...
    def create_reference(self) -> typing.Optional[IMemoryBufferReference]: ...

class PropertyValue(toasts_winrt.system.Object):
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> PropertyValue: ...
    @staticmethod
    def create_boolean(value: toasts_winrt.system.Boolean, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_boolean_array(value: toasts_winrt.system.Array[toasts_winrt.system.Boolean], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_char16(value: toasts_winrt.system.Char16, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_char16_array(value: toasts_winrt.system.Array[toasts_winrt.system.Char16], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_date_time(value: datetime.datetime, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_date_time_array(value: toasts_winrt.system.Array[datetime.datetime], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_double(value: toasts_winrt.system.Double, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_double_array(value: toasts_winrt.system.Array[toasts_winrt.system.Double], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_empty() -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_guid(value: toasts_winrt.system.Guid, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_guid_array(value: toasts_winrt.system.Array[toasts_winrt.system.Guid], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_inspectable(value: typing.Optional[toasts_winrt.system.Object], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_inspectable_array(value: toasts_winrt.system.Array[toasts_winrt.system.Object], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int16(value: toasts_winrt.system.Int16, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int16_array(value: toasts_winrt.system.Array[toasts_winrt.system.Int16], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int32(value: toasts_winrt.system.Int32, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int32_array(value: toasts_winrt.system.Array[toasts_winrt.system.Int32], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int64(value: toasts_winrt.system.Int64, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_int64_array(value: toasts_winrt.system.Array[toasts_winrt.system.Int64], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_point(value: Point, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_point_array(value: toasts_winrt.system.Array[Point], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_rect(value: Rect, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_rect_array(value: toasts_winrt.system.Array[Rect], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_single(value: toasts_winrt.system.Single, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_single_array(value: toasts_winrt.system.Array[toasts_winrt.system.Single], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_size(value: Size, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_size_array(value: toasts_winrt.system.Array[Size], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_string(value: str, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_string_array(value: toasts_winrt.system.Array[str], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_time_span(value: datetime.timedelta, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_time_span_array(value: toasts_winrt.system.Array[datetime.timedelta], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint16(value: toasts_winrt.system.UInt16, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint16_array(value: toasts_winrt.system.Array[toasts_winrt.system.UInt16], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint32(value: toasts_winrt.system.UInt32, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint32_array(value: toasts_winrt.system.Array[toasts_winrt.system.UInt32], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint64(value: toasts_winrt.system.UInt64, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint64_array(value: toasts_winrt.system.Array[toasts_winrt.system.UInt64], /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint8(value: toasts_winrt.system.UInt8, /) -> typing.Optional[toasts_winrt.system.Object]: ...
    @staticmethod
    def create_uint8_array(value: toasts_winrt.system.Array[toasts_winrt.system.UInt8], /) -> typing.Optional[toasts_winrt.system.Object]: ...

class Uri(toasts_winrt.system.Object):
    absolute_uri: str
    display_uri: str
    domain: str
    extension: str
    fragment: str
    host: str
    password: str
    path: str
    port: toasts_winrt.system.Int32
    query: str
    query_parsed: typing.Optional[WwwFormUrlDecoder]
    raw_uri: str
    scheme_name: str
    suspicious: toasts_winrt.system.Boolean
    user_name: str
    absolute_canonical_uri: str
    display_iri: str
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> Uri: ...
    @typing.overload
    def __new__(cls: typing.Type[Uri], uri: str) -> Uri:...
    @typing.overload
    def __new__(cls: typing.Type[Uri], base_uri: str, relative_uri: str) -> Uri:...
    def combine_uri(self, relative_uri: str, /) -> typing.Optional[Uri]: ...
    def equals(self, p_uri: typing.Optional[Uri], /) -> toasts_winrt.system.Boolean: ...
    @staticmethod
    def escape_component(to_escape: str, /) -> str: ...
    def to_string(self) -> str: ...
    @staticmethod
    def unescape_component(to_unescape: str, /) -> str: ...

class WwwFormUrlDecoder(toasts_winrt.system.Object, typing.Sequence[IWwwFormUrlDecoderEntry]):
    size: toasts_winrt.system.UInt32
    def __len__(self) -> int: ...
    @typing.overload
    def __getitem__(self, index: int) -> IWwwFormUrlDecoderEntry: ...
    @typing.overload
    def __getitem__(self, index: slice) -> toasts_winrt.system.Array[IWwwFormUrlDecoderEntry]: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> WwwFormUrlDecoder: ...
    def __new__(cls: typing.Type[WwwFormUrlDecoder], query: str) -> WwwFormUrlDecoder:...
    def first(self) -> typing.Optional[toasts_winrt.windows.foundation.collections.IIterator[IWwwFormUrlDecoderEntry]]: ...
    def get_at(self, index: toasts_winrt.system.UInt32, /) -> typing.Optional[IWwwFormUrlDecoderEntry]: ...
    def get_first_value_by_name(self, name: str, /) -> str: ...
    def get_many(self, start_index: toasts_winrt.system.UInt32, items: toasts_winrt.system.Array[IWwwFormUrlDecoderEntry], /) -> toasts_winrt.system.UInt32: ...
    def index_of(self, value: typing.Optional[IWwwFormUrlDecoderEntry], /) -> typing.Tuple[toasts_winrt.system.Boolean, toasts_winrt.system.UInt32]: ...

class WwwFormUrlDecoderEntry(toasts_winrt.system.Object):
    name: str
    value: str
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> WwwFormUrlDecoderEntry: ...

class IAsyncAction(toasts_winrt.system.Object):
    completed: typing.Optional[AsyncActionCompletedHandler]
    error_code: HResult
    id: toasts_winrt.system.UInt32
    status: AsyncStatus
    def __await__(self) -> typing.Generator[typing.Any, None, None]: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IAsyncAction: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> None: ...

class IAsyncActionWithProgress(toasts_winrt.system.Object, typing.Generic[TProgress]):
    progress: typing.Optional[AsyncActionProgressHandler[TProgress]]
    completed: typing.Optional[AsyncActionWithProgressCompletedHandler[TProgress]]
    error_code: HResult
    id: toasts_winrt.system.UInt32
    status: AsyncStatus
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, key: typing.Any) -> types.GenericAlias: ...
    def __await__(self) -> typing.Generator[typing.Any, None, None]: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> None: ...

class IAsyncInfo(toasts_winrt.system.Object):
    error_code: HResult
    id: toasts_winrt.system.UInt32
    status: AsyncStatus
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IAsyncInfo: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...

class IAsyncOperationWithProgress(toasts_winrt.system.Object, typing.Generic[TResult, TProgress]):
    progress: typing.Optional[AsyncOperationProgressHandler[TResult, TProgress]]
    completed: typing.Optional[AsyncOperationWithProgressCompletedHandler[TResult, TProgress]]
    error_code: HResult
    id: toasts_winrt.system.UInt32
    status: AsyncStatus
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, key: typing.Any) -> types.GenericAlias: ...
    def __await__(self) -> typing.Generator[typing.Any, None, TResult]: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> typing.Optional[TResult]: ...

class IAsyncOperation(toasts_winrt.system.Object, typing.Generic[TResult]):
    completed: typing.Optional[AsyncOperationCompletedHandler[TResult]]
    error_code: HResult
    id: toasts_winrt.system.UInt32
    status: AsyncStatus
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, key: typing.Any) -> types.GenericAlias: ...
    def __await__(self) -> typing.Generator[typing.Any, None, TResult]: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def get_results(self) -> typing.Optional[TResult]: ...

class IClosable(toasts_winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IClosable: ...
    def close(self) -> None: ...

class IGetActivationFactory(toasts_winrt.system.Object):
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IGetActivationFactory: ...
    def get_activation_factory(self, activatable_class_id: str, /) -> typing.Optional[toasts_winrt.system.Object]: ...

class IMemoryBuffer(toasts_winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IMemoryBuffer: ...
    def close(self) -> None: ...
    def create_reference(self) -> typing.Optional[IMemoryBufferReference]: ...

class IMemoryBufferReference(toasts_winrt.system.Object):
    capacity: toasts_winrt.system.UInt32
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    def __buffer__(self, flags: int) -> memoryview: ...
    def __release_buffer__(self, view: memoryview) -> None: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IMemoryBufferReference: ...
    def close(self) -> None: ...
    def add_closed(self, handler: TypedEventHandler[IMemoryBufferReference, toasts_winrt.system.Object], /) -> EventRegistrationToken: ...
    def remove_closed(self, cookie: EventRegistrationToken, /) -> None: ...

class IPropertyValue(toasts_winrt.system.Object):
    is_numeric_scalar: toasts_winrt.system.Boolean
    type: PropertyType
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IPropertyValue: ...
    def get_boolean(self) -> toasts_winrt.system.Boolean: ...
    def get_boolean_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Boolean]: ...
    def get_char16(self) -> toasts_winrt.system.Char16: ...
    def get_char16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Char16]: ...
    def get_date_time(self) -> datetime.datetime: ...
    def get_date_time_array(self) -> toasts_winrt.system.Array[datetime.datetime]: ...
    def get_double(self) -> toasts_winrt.system.Double: ...
    def get_double_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Double]: ...
    def get_guid(self) -> toasts_winrt.system.Guid: ...
    def get_guid_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Guid]: ...
    def get_inspectable_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Object]: ...
    def get_int16(self) -> toasts_winrt.system.Int16: ...
    def get_int16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int16]: ...
    def get_int32(self) -> toasts_winrt.system.Int32: ...
    def get_int32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int32]: ...
    def get_int64(self) -> toasts_winrt.system.Int64: ...
    def get_int64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int64]: ...
    def get_point(self) -> Point: ...
    def get_point_array(self) -> toasts_winrt.system.Array[Point]: ...
    def get_rect(self) -> Rect: ...
    def get_rect_array(self) -> toasts_winrt.system.Array[Rect]: ...
    def get_single(self) -> toasts_winrt.system.Single: ...
    def get_single_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Single]: ...
    def get_size(self) -> Size: ...
    def get_size_array(self) -> toasts_winrt.system.Array[Size]: ...
    def get_string(self) -> str: ...
    def get_string_array(self) -> toasts_winrt.system.Array[str]: ...
    def get_time_span(self) -> datetime.timedelta: ...
    def get_time_span_array(self) -> toasts_winrt.system.Array[datetime.timedelta]: ...
    def get_uint16(self) -> toasts_winrt.system.UInt16: ...
    def get_uint16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt16]: ...
    def get_uint32(self) -> toasts_winrt.system.UInt32: ...
    def get_uint32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt32]: ...
    def get_uint64(self) -> toasts_winrt.system.UInt64: ...
    def get_uint64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt64]: ...
    def get_uint8(self) -> toasts_winrt.system.UInt8: ...
    def get_uint8_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt8]: ...

class IReferenceArray(toasts_winrt.system.Object, typing.Generic[T]):
    value: typing.Optional[T]
    is_numeric_scalar: toasts_winrt.system.Boolean
    type: PropertyType
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, key: typing.Any) -> types.GenericAlias: ...
    def get_boolean(self) -> toasts_winrt.system.Boolean: ...
    def get_boolean_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Boolean]: ...
    def get_char16(self) -> toasts_winrt.system.Char16: ...
    def get_char16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Char16]: ...
    def get_date_time(self) -> datetime.datetime: ...
    def get_date_time_array(self) -> toasts_winrt.system.Array[datetime.datetime]: ...
    def get_double(self) -> toasts_winrt.system.Double: ...
    def get_double_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Double]: ...
    def get_guid(self) -> toasts_winrt.system.Guid: ...
    def get_guid_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Guid]: ...
    def get_inspectable_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Object]: ...
    def get_int16(self) -> toasts_winrt.system.Int16: ...
    def get_int16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int16]: ...
    def get_int32(self) -> toasts_winrt.system.Int32: ...
    def get_int32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int32]: ...
    def get_int64(self) -> toasts_winrt.system.Int64: ...
    def get_int64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int64]: ...
    def get_point(self) -> Point: ...
    def get_point_array(self) -> toasts_winrt.system.Array[Point]: ...
    def get_rect(self) -> Rect: ...
    def get_rect_array(self) -> toasts_winrt.system.Array[Rect]: ...
    def get_single(self) -> toasts_winrt.system.Single: ...
    def get_single_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Single]: ...
    def get_size(self) -> Size: ...
    def get_size_array(self) -> toasts_winrt.system.Array[Size]: ...
    def get_string(self) -> str: ...
    def get_string_array(self) -> toasts_winrt.system.Array[str]: ...
    def get_time_span(self) -> datetime.timedelta: ...
    def get_time_span_array(self) -> toasts_winrt.system.Array[datetime.timedelta]: ...
    def get_uint16(self) -> toasts_winrt.system.UInt16: ...
    def get_uint16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt16]: ...
    def get_uint32(self) -> toasts_winrt.system.UInt32: ...
    def get_uint32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt32]: ...
    def get_uint64(self) -> toasts_winrt.system.UInt64: ...
    def get_uint64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt64]: ...
    def get_uint8(self) -> toasts_winrt.system.UInt8: ...
    def get_uint8_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt8]: ...

class IReference(toasts_winrt.system.Object, typing.Generic[T]):
    value: typing.Optional[T]
    is_numeric_scalar: toasts_winrt.system.Boolean
    type: PropertyType
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, key: typing.Any) -> types.GenericAlias: ...
    def get_boolean(self) -> toasts_winrt.system.Boolean: ...
    def get_boolean_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Boolean]: ...
    def get_char16(self) -> toasts_winrt.system.Char16: ...
    def get_char16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Char16]: ...
    def get_date_time(self) -> datetime.datetime: ...
    def get_date_time_array(self) -> toasts_winrt.system.Array[datetime.datetime]: ...
    def get_double(self) -> toasts_winrt.system.Double: ...
    def get_double_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Double]: ...
    def get_guid(self) -> toasts_winrt.system.Guid: ...
    def get_guid_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Guid]: ...
    def get_inspectable_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Object]: ...
    def get_int16(self) -> toasts_winrt.system.Int16: ...
    def get_int16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int16]: ...
    def get_int32(self) -> toasts_winrt.system.Int32: ...
    def get_int32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int32]: ...
    def get_int64(self) -> toasts_winrt.system.Int64: ...
    def get_int64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Int64]: ...
    def get_point(self) -> Point: ...
    def get_point_array(self) -> toasts_winrt.system.Array[Point]: ...
    def get_rect(self) -> Rect: ...
    def get_rect_array(self) -> toasts_winrt.system.Array[Rect]: ...
    def get_single(self) -> toasts_winrt.system.Single: ...
    def get_single_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.Single]: ...
    def get_size(self) -> Size: ...
    def get_size_array(self) -> toasts_winrt.system.Array[Size]: ...
    def get_string(self) -> str: ...
    def get_string_array(self) -> toasts_winrt.system.Array[str]: ...
    def get_time_span(self) -> datetime.timedelta: ...
    def get_time_span_array(self) -> toasts_winrt.system.Array[datetime.timedelta]: ...
    def get_uint16(self) -> toasts_winrt.system.UInt16: ...
    def get_uint16_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt16]: ...
    def get_uint32(self) -> toasts_winrt.system.UInt32: ...
    def get_uint32_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt32]: ...
    def get_uint64(self) -> toasts_winrt.system.UInt64: ...
    def get_uint64_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt64]: ...
    def get_uint8(self) -> toasts_winrt.system.UInt8: ...
    def get_uint8_array(self) -> toasts_winrt.system.Array[toasts_winrt.system.UInt8]: ...

class IStringable(toasts_winrt.system.Object):
    def __str__(self) -> str: ...
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IStringable: ...
    def to_string(self) -> str: ...

class IWwwFormUrlDecoderEntry(toasts_winrt.system.Object):
    name: str
    value: str
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> IWwwFormUrlDecoderEntry: ...

AsyncActionCompletedHandler = typing.Callable[[IAsyncAction, AsyncStatus], None]

AsyncActionProgressHandler = typing.Callable[[IAsyncActionWithProgress[TProgress], typing.Optional[TProgress]], None]

AsyncActionWithProgressCompletedHandler = typing.Callable[[IAsyncActionWithProgress[TProgress], AsyncStatus], None]

AsyncOperationCompletedHandler = typing.Callable[[IAsyncOperation[TResult], AsyncStatus], None]

AsyncOperationProgressHandler = typing.Callable[[IAsyncOperationWithProgress[TResult, TProgress], typing.Optional[TProgress]], None]

AsyncOperationWithProgressCompletedHandler = typing.Callable[[IAsyncOperationWithProgress[TResult, TProgress], AsyncStatus], None]

DeferralCompletedHandler = typing.Callable[[], None]

EventHandler = typing.Callable[[typing.Optional[toasts_winrt.system.Object], typing.Optional[T]], None]

TypedEventHandler = typing.Callable[[typing.Optional[TSender], typing.Optional[TResult]], None]

