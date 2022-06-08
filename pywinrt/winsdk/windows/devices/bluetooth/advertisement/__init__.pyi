# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.devices.bluetooth
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams

class BluetoothLEAdvertisementFlags(enum.IntFlag):
    NONE = 0
    LIMITED_DISCOVERABLE_MODE = 0x1
    GENERAL_DISCOVERABLE_MODE = 0x2
    CLASSIC_NOT_SUPPORTED = 0x4
    DUAL_MODE_CONTROLLER_CAPABLE = 0x8
    DUAL_MODE_HOST_CAPABLE = 0x10

class BluetoothLEAdvertisementPublisherStatus(enum.IntEnum):
    CREATED = 0
    WAITING = 1
    STARTED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class BluetoothLEAdvertisementType(enum.IntEnum):
    CONNECTABLE_UNDIRECTED = 0
    CONNECTABLE_DIRECTED = 1
    SCANNABLE_UNDIRECTED = 2
    NON_CONNECTABLE_UNDIRECTED = 3
    SCAN_RESPONSE = 4
    EXTENDED = 5

class BluetoothLEAdvertisementWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    STOPPING = 2
    STOPPED = 3
    ABORTED = 4

class BluetoothLEScanningMode(enum.IntEnum):
    PASSIVE = 0
    ACTIVE = 1
    NONE = 2

Self = typing.TypeVar('Self')

class BluetoothLEAdvertisement(_winrt.Object):
    local_name: str
    flags: typing.Optional[typing.Optional[BluetoothLEAdvertisementFlags]]
    data_sections: typing.Optional[winsdk.windows.foundation.collections.IVector[BluetoothLEAdvertisementDataSection]]
    manufacturer_data: typing.Optional[winsdk.windows.foundation.collections.IVector[BluetoothLEManufacturerData]]
    service_uuids: typing.Optional[winsdk.windows.foundation.collections.IVector[uuid.UUID]]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisement: ...
    def __init__(self) -> None: ...
    def get_manufacturer_data_by_company_id(self, company_id: _winrt.UInt16) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[BluetoothLEManufacturerData]]: ...
    def get_sections_by_type(self, type: _winrt.UInt8) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[BluetoothLEAdvertisementDataSection]]: ...

class BluetoothLEAdvertisementBytePattern(_winrt.Object):
    offset: _winrt.Int16
    data_type: _winrt.UInt8
    data: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementBytePattern: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, data_type: _winrt.UInt8, offset: _winrt.Int16, data: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> None: ...

class BluetoothLEAdvertisementDataSection(_winrt.Object):
    data_type: _winrt.UInt8
    data: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementDataSection: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, data_type: _winrt.UInt8, data: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> None: ...

class BluetoothLEAdvertisementDataTypes(_winrt.Object):
    advertising_interval: _winrt.UInt8
    appearance: _winrt.UInt8
    complete_local_name: _winrt.UInt8
    complete_service128_bit_uuids: _winrt.UInt8
    complete_service16_bit_uuids: _winrt.UInt8
    complete_service32_bit_uuids: _winrt.UInt8
    flags: _winrt.UInt8
    incomplete_service128_bit_uuids: _winrt.UInt8
    incomplete_service16_bit_uuids: _winrt.UInt8
    incomplete_service32_bit_uuids: _winrt.UInt8
    manufacturer_specific_data: _winrt.UInt8
    peripheral_connection_interval_range: _winrt.UInt8
    public_target_address: _winrt.UInt8
    random_target_address: _winrt.UInt8
    service_data128_bit_uuids: _winrt.UInt8
    service_data16_bit_uuids: _winrt.UInt8
    service_data32_bit_uuids: _winrt.UInt8
    service_solicitation128_bit_uuids: _winrt.UInt8
    service_solicitation16_bit_uuids: _winrt.UInt8
    service_solicitation32_bit_uuids: _winrt.UInt8
    shortened_local_name: _winrt.UInt8
    tx_power_level: _winrt.UInt8
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementDataTypes: ...

class BluetoothLEAdvertisementFilter(_winrt.Object):
    advertisement: typing.Optional[BluetoothLEAdvertisement]
    byte_patterns: typing.Optional[winsdk.windows.foundation.collections.IVector[BluetoothLEAdvertisementBytePattern]]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementFilter: ...
    def __init__(self) -> None: ...

class BluetoothLEAdvertisementPublisher(_winrt.Object):
    advertisement: typing.Optional[BluetoothLEAdvertisement]
    status: BluetoothLEAdvertisementPublisherStatus
    use_extended_advertisement: _winrt.Boolean
    preferred_transmit_power_level_in_d_bm: typing.Optional[typing.Optional[_winrt.Int16]]
    is_anonymous: _winrt.Boolean
    include_transmit_power_level: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementPublisher: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, advertisement: typing.Optional[BluetoothLEAdvertisement]) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEAdvertisementPublisher, BluetoothLEAdvertisementPublisherStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class BluetoothLEAdvertisementPublisherStatusChangedEventArgs(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    status: BluetoothLEAdvertisementPublisherStatus
    selected_transmit_power_level_in_d_bm: typing.Optional[typing.Optional[_winrt.Int16]]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementPublisherStatusChangedEventArgs: ...

class BluetoothLEAdvertisementReceivedEventArgs(_winrt.Object):
    advertisement: typing.Optional[BluetoothLEAdvertisement]
    advertisement_type: BluetoothLEAdvertisementType
    bluetooth_address: _winrt.UInt64
    raw_signal_strength_in_d_bm: _winrt.Int16
    timestamp: winsdk.windows.foundation.DateTime
    bluetooth_address_type: winsdk.windows.devices.bluetooth.BluetoothAddressType
    is_anonymous: _winrt.Boolean
    is_connectable: _winrt.Boolean
    is_directed: _winrt.Boolean
    is_scan_response: _winrt.Boolean
    is_scannable: _winrt.Boolean
    transmit_power_level_in_d_bm: typing.Optional[typing.Optional[_winrt.Int16]]
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementReceivedEventArgs: ...

class BluetoothLEAdvertisementWatcher(_winrt.Object):
    signal_strength_filter: typing.Optional[winsdk.windows.devices.bluetooth.BluetoothSignalStrengthFilter]
    scanning_mode: BluetoothLEScanningMode
    advertisement_filter: typing.Optional[BluetoothLEAdvertisementFilter]
    max_out_of_range_timeout: winsdk.windows.foundation.TimeSpan
    max_sampling_interval: winsdk.windows.foundation.TimeSpan
    min_out_of_range_timeout: winsdk.windows.foundation.TimeSpan
    min_sampling_interval: winsdk.windows.foundation.TimeSpan
    status: BluetoothLEAdvertisementWatcherStatus
    allow_extended_advertisements: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementWatcher: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, advertisement_filter: typing.Optional[BluetoothLEAdvertisementFilter]) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_received(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEAdvertisementWatcher, BluetoothLEAdvertisementReceivedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_received(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_stopped(self, handler: winsdk.windows.foundation.TypedEventHandler[BluetoothLEAdvertisementWatcher, BluetoothLEAdvertisementWatcherStoppedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_stopped(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class BluetoothLEAdvertisementWatcherStoppedEventArgs(_winrt.Object):
    error: winsdk.windows.devices.bluetooth.BluetoothError
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEAdvertisementWatcherStoppedEventArgs: ...

class BluetoothLEManufacturerData(_winrt.Object):
    data: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    company_id: _winrt.UInt16
    @staticmethod
    def _from(obj: _winrt.Object) -> BluetoothLEManufacturerData: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, company_id: _winrt.UInt16, data: typing.Optional[winsdk.windows.storage.streams.IBuffer]) -> None: ...

