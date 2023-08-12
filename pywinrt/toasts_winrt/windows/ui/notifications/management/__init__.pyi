# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.10

import enum
import datetime
import sys
import types
import typing

import toasts_winrt.system
import toasts_winrt.windows.foundation
import toasts_winrt.windows.foundation.collections
import toasts_winrt.windows.ui.notifications

class UserNotificationListenerAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED = 2

Self = typing.TypeVar('Self')

class UserNotificationListener(toasts_winrt.system.Object):
    current: typing.ClassVar[typing.Optional[UserNotificationListener]]
    @staticmethod
    def _from(obj: toasts_winrt.system.Object, /) -> UserNotificationListener: ...
    def clear_notifications(self) -> None: ...
    def get_access_status(self) -> UserNotificationListenerAccessStatus: ...
    def get_notification(self, notification_id: toasts_winrt.system.UInt32, /) -> typing.Optional[toasts_winrt.windows.ui.notifications.UserNotification]: ...
    def get_notifications_async(self, kinds: toasts_winrt.windows.ui.notifications.NotificationKinds, /) -> toasts_winrt.windows.foundation.IAsyncOperation[toasts_winrt.windows.foundation.collections.IVectorView[toasts_winrt.windows.ui.notifications.UserNotification]]: ...
    def remove_notification(self, notification_id: toasts_winrt.system.UInt32, /) -> None: ...
    def request_access_async(self) -> toasts_winrt.windows.foundation.IAsyncOperation[UserNotificationListenerAccessStatus]: ...
    def add_notification_changed(self, handler: toasts_winrt.windows.foundation.TypedEventHandler[UserNotificationListener, toasts_winrt.windows.ui.notifications.UserNotificationChangedEventArgs], /) -> toasts_winrt.windows.foundation.EventRegistrationToken: ...
    def remove_notification_changed(self, token: toasts_winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

