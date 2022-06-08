# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections

class WindowsUpdateAdministratorOptions(enum.IntFlag):
    NONE = 0
    REQUIRE_ADMINISTRATOR_APPROVAL_FOR_SCANS = 0x1
    REQUIRE_ADMINISTRATOR_APPROVAL_FOR_UPDATES = 0x2
    REQUIRE_ADMINISTRATOR_APPROVAL_FOR_ACTIONS = 0x4

class WindowsUpdateAdministratorStatus(enum.IntEnum):
    SUCCEEDED = 0
    NO_ADMINISTRATOR_REGISTERED = 1
    OTHER_ADMINISTRATOR_IS_REGISTERED = 2

class WindowsUpdateAttentionRequiredReason(enum.IntEnum):
    NONE = 0
    SEEKER_UPDATE = 1
    READY_TO_REBOOT = 2
    NEED_NON_METERED_NETWORK = 3
    NEED_USER_AGREEMENT_FOR_METERED_NETWORK = 4
    NEED_NETWORK = 5
    NEED_MORE_SPACE = 6
    BATTERY_SAVER_ENABLED = 7
    NEED_USER_INTERACTION = 8
    NEED_USER_AGREEMENT_FOR_POLICY = 9
    COMPATIBILITY_ERROR = 10
    NEED_USER_INTERACTION_FOR_EULA = 11
    NEED_USER_INTERACTION_FOR_CTA = 12
    REGULATED = 13
    EXTERNAL_REBOOT = 14
    OTHER_UPDATE = 15
    BLOCKED_BY_PROVIDER = 16
    BLOCKED_BY_POST_REBOOT_FAILURE = 17
    USER_ENGAGED = 18
    BLOCKED_BY_BATTERY = 19
    EXCLUSIVITY = 20
    BLOCKED_BY_SERIALIZATION = 21
    CONFLICT_CLASS = 22
    BLOCKED_BY_ADMIN_APPROVAL = 23
    BLOCKED_BY_TOO_MANY_ATTEMPTS = 24
    BLOCKED_BY_FAILURE = 25
    DEMOTION = 26
    BLOCKED_BY_ACTIVE_HOURS = 27
    SCHEDULED_FOR_MAINTENANCE = 28
    POLICY_SCHEDULED_INSTALL_TIME = 29
    BLOCKED_BY_OOBE = 30
    DEFERRED_DURING_OOBE = 31
    DEFERRED_FOR_SUSTAINABLE_TIME = 32

Self = typing.TypeVar('Self')

class PreviewBuildsManager(_winrt.Object):
    are_preview_builds_allowed: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PreviewBuildsManager: ...
    def get_current_state(self) -> typing.Optional[PreviewBuildsState]: ...
    @staticmethod
    def get_default() -> typing.Optional[PreviewBuildsManager]: ...
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    def sync_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class PreviewBuildsState(_winrt.Object):
    properties: typing.Optional[winsdk.windows.foundation.collections.ValueSet]
    @staticmethod
    def _from(obj: _winrt.Object) -> PreviewBuildsState: ...

class WindowsUpdate(_winrt.Object):
    action_progress: typing.Optional[WindowsUpdateActionProgress]
    action_result: typing.Optional[WindowsUpdateActionResult]
    attention_required_info: typing.Optional[WindowsUpdateAttentionRequiredInfo]
    current_action: str
    deadline: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    description: str
    eula_text: str
    is_critical: _winrt.Boolean
    is_driver: _winrt.Boolean
    is_eula_accepted: _winrt.Boolean
    is_feature_update: _winrt.Boolean
    is_for_o_s: _winrt.Boolean
    is_mandatory: _winrt.Boolean
    is_minor_impact: _winrt.Boolean
    is_security: _winrt.Boolean
    is_seeker: _winrt.Boolean
    is_urgent: _winrt.Boolean
    more_info_url: typing.Optional[winsdk.windows.foundation.Uri]
    provider_id: str
    support_url: typing.Optional[winsdk.windows.foundation.Uri]
    title: str
    update_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdate: ...
    def accept_eula(self) -> None: ...
    def get_property_value(self, property_name: str) -> typing.Optional[_winrt.Object]: ...

class WindowsUpdateActionCompletedEventArgs(_winrt.Object):
    action: str
    extended_error: winsdk.windows.foundation.HResult
    succeeded: _winrt.Boolean
    update: typing.Optional[WindowsUpdate]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateActionCompletedEventArgs: ...

class WindowsUpdateActionProgress(_winrt.Object):
    action: str
    progress: _winrt.Double
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateActionProgress: ...

class WindowsUpdateActionResult(_winrt.Object):
    action: str
    extended_error: winsdk.windows.foundation.HResult
    succeeded: _winrt.Boolean
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateActionResult: ...

class WindowsUpdateAdministrator(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateAdministrator: ...
    def approve_windows_update(self, update_id: str, approval_data: typing.Optional[WindowsUpdateApprovalData]) -> None: ...
    def approve_windows_update_action(self, update_id: str, action: str) -> None: ...
    @staticmethod
    def cancel_restart_request(request_restart_token: str) -> None: ...
    @staticmethod
    def get_registered_administrator(organization_name: str) -> typing.Optional[WindowsUpdateGetAdministratorResult]: ...
    @staticmethod
    def get_registered_administrator_name() -> str: ...
    def get_updates(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[WindowsUpdate]]: ...
    @staticmethod
    def register_for_administration(organization_name: str, options: WindowsUpdateAdministratorOptions) -> WindowsUpdateAdministratorStatus: ...
    @staticmethod
    def request_restart(restart_options: typing.Optional[WindowsUpdateRestartRequestOptions]) -> str: ...
    def revoke_windows_update_action_approval(self, update_id: str, action: str) -> None: ...
    def revoke_windows_update_approval(self, update_id: str) -> None: ...
    def start_administrator_scan(self) -> None: ...
    @staticmethod
    def unregister_for_administration(organization_name: str) -> WindowsUpdateAdministratorStatus: ...

class WindowsUpdateApprovalData(_winrt.Object):
    seeker: typing.Optional[typing.Optional[_winrt.Boolean]]
    opt_out_of_auto_reboot: typing.Optional[typing.Optional[_winrt.Boolean]]
    compliance_grace_period_in_days: typing.Optional[typing.Optional[_winrt.Int32]]
    compliance_deadline_in_days: typing.Optional[typing.Optional[_winrt.Int32]]
    allow_download_on_metered: typing.Optional[typing.Optional[_winrt.Boolean]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateApprovalData: ...
    def __init__(self) -> None: ...

class WindowsUpdateAttentionRequiredInfo(_winrt.Object):
    reason: WindowsUpdateAttentionRequiredReason
    timestamp: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateAttentionRequiredInfo: ...

class WindowsUpdateAttentionRequiredReasonChangedEventArgs(_winrt.Object):
    reason: WindowsUpdateAttentionRequiredReason
    update: typing.Optional[WindowsUpdate]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateAttentionRequiredReasonChangedEventArgs: ...

class WindowsUpdateGetAdministratorResult(_winrt.Object):
    administrator: typing.Optional[WindowsUpdateAdministrator]
    status: WindowsUpdateAdministratorStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateGetAdministratorResult: ...

class WindowsUpdateItem(_winrt.Object):
    category: str
    description: str
    more_info_url: typing.Optional[winsdk.windows.foundation.Uri]
    operation: str
    provider_id: str
    timestamp: winsdk.windows.foundation.DateTime
    title: str
    update_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateItem: ...

class WindowsUpdateManager(_winrt.Object):
    is_scanning: _winrt.Boolean
    is_working: _winrt.Boolean
    last_successful_scan_timestamp: typing.Optional[typing.Optional[winsdk.windows.foundation.DateTime]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateManager: ...
    def __init__(self, client_id: str) -> None: ...
    def get_applicable_updates(self) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[WindowsUpdate]]: ...
    def get_most_recent_completed_updates(self, count: _winrt.Int32) -> typing.Optional[winsdk.windows.foundation.collections.IVectorView[WindowsUpdateItem]]: ...
    def get_most_recent_completed_updates_async(self, count: _winrt.Int32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[WindowsUpdateItem]]: ...
    def start_scan(self, user_initiated: _winrt.Boolean) -> None: ...
    def add_action_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, WindowsUpdateActionCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_action_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_attention_required_reason_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, WindowsUpdateAttentionRequiredReasonChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_attention_required_reason_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_progress_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, WindowsUpdateProgressChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_progress_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_scan_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, WindowsUpdateScanCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_scan_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_scanning_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_scanning_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_working_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[WindowsUpdateManager, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_working_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class WindowsUpdateProgressChangedEventArgs(_winrt.Object):
    action_progress: typing.Optional[WindowsUpdateActionProgress]
    update: typing.Optional[WindowsUpdate]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateProgressChangedEventArgs: ...

class WindowsUpdateRestartRequestOptions(_winrt.Object):
    title: str
    organization_name: str
    opt_out_of_auto_reboot: _winrt.Boolean
    more_info_url: typing.Optional[winsdk.windows.foundation.Uri]
    description: str
    compliance_grace_period_in_days: _winrt.Int32
    compliance_deadline_in_days: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateRestartRequestOptions: ...
    @typing.overload
    def __init__(self, title: str, description: str, more_info_url: typing.Optional[winsdk.windows.foundation.Uri], compliance_deadline_in_days: _winrt.Int32, compliance_grace_period_in_days: _winrt.Int32) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...

class WindowsUpdateScanCompletedEventArgs(_winrt.Object):
    extended_error: winsdk.windows.foundation.HResult
    provider_id: str
    succeeded: _winrt.Boolean
    updates: typing.Optional[winsdk.windows.foundation.collections.IVectorView[WindowsUpdate]]
    @staticmethod
    def _from(obj: _winrt.Object) -> WindowsUpdateScanCompletedEventArgs: ...

