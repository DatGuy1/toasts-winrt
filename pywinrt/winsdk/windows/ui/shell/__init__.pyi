# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel.core
import winsdk.windows.foundation
import winsdk.windows.ui
import winsdk.windows.ui.startscreen

class SecurityAppKind(enum.IntEnum):
    WEB_PROTECTION = 0

class SecurityAppState(enum.IntEnum):
    DISABLED = 0
    ENABLED = 1

class SecurityAppSubstatus(enum.IntEnum):
    UNDETERMINED = 0
    NO_ACTION_NEEDED = 1
    ACTION_RECOMMENDED = 2
    ACTION_NEEDED = 3

class ShareWindowCommand(enum.IntEnum):
    NONE = 0
    START_SHARING = 1
    STOP_SHARING = 2

Self = typing.TypeVar('Self')

class AdaptiveCardBuilder(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AdaptiveCardBuilder: ...
    @staticmethod
    def create_adaptive_card_from_json(value: str) -> typing.Optional[IAdaptiveCard]: ...

class FocusSession(_winrt.Object):
    id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> FocusSession: ...
    def end(self) -> None: ...

class FocusSessionManager(_winrt.Object):
    is_focus_active: _winrt.Boolean
    is_supported: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> FocusSessionManager: ...
    def deactivate_focus(self) -> None: ...
    @staticmethod
    def get_default() -> typing.Optional[FocusSessionManager]: ...
    def get_session(self, id: str) -> typing.Optional[FocusSession]: ...
    @typing.overload
    def try_start_focus_session(self) -> typing.Optional[FocusSession]: ...
    @typing.overload
    def try_start_focus_session(self, end_time: winsdk.windows.foundation.DateTime) -> typing.Optional[FocusSession]: ...
    def add_is_focus_active_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[FocusSessionManager, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_is_focus_active_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SecurityAppManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SecurityAppManager: ...
    def __init__(self) -> None: ...
    def register(self, kind: SecurityAppKind, display_name: str, details_uri: typing.Optional[winsdk.windows.foundation.Uri], register_per_user: _winrt.Boolean) -> uuid.UUID: ...
    def unregister(self, kind: SecurityAppKind, guid_registration: uuid.UUID) -> None: ...
    def update_state(self, kind: SecurityAppKind, guid_registration: uuid.UUID, state: SecurityAppState, substatus: SecurityAppSubstatus, details_uri: typing.Optional[winsdk.windows.foundation.Uri]) -> None: ...

class ShareWindowCommandEventArgs(_winrt.Object):
    command: ShareWindowCommand
    window_id: winsdk.windows.ui.WindowId
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareWindowCommandEventArgs: ...

class ShareWindowCommandSource(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareWindowCommandSource: ...
    @staticmethod
    def get_for_current_view() -> typing.Optional[ShareWindowCommandSource]: ...
    def report_command_changed(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_command_invoked(self, handler: winsdk.windows.foundation.TypedEventHandler[ShareWindowCommandSource, ShareWindowCommandEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_command_invoked(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_command_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[ShareWindowCommandSource, ShareWindowCommandEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_command_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class TaskbarManager(_winrt.Object):
    is_pinning_allowed: _winrt.Boolean
    is_supported: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> TaskbarManager: ...
    @staticmethod
    def get_default() -> typing.Optional[TaskbarManager]: ...
    def is_app_list_entry_pinned_async(self, app_list_entry: typing.Optional[winsdk.windows.applicationmodel.core.AppListEntry]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def is_current_app_pinned_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def is_secondary_tile_pinned_async(self, tile_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def request_pin_app_list_entry_async(self, app_list_entry: typing.Optional[winsdk.windows.applicationmodel.core.AppListEntry]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def request_pin_current_app_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def request_pin_secondary_tile_async(self, secondary_tile: typing.Optional[winsdk.windows.ui.startscreen.SecondaryTile]) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    def try_unpin_secondary_tile_async(self, tile_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class IAdaptiveCard(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IAdaptiveCard: ...
    def to_json(self) -> str: ...

class IAdaptiveCardBuilderStatics(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IAdaptiveCardBuilderStatics: ...
    def create_adaptive_card_from_json(self, value: str) -> typing.Optional[IAdaptiveCard]: ...

