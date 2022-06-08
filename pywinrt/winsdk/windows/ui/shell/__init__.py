# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.UI.Shell")

try:
    import winsdk.windows.applicationmodel.core
except ImportError:
    pass

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.ui
except ImportError:
    pass

try:
    import winsdk.windows.ui.startscreen
except ImportError:
    pass

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

_ns_module._register_SecurityAppKind(SecurityAppKind)
_ns_module._register_SecurityAppState(SecurityAppState)
_ns_module._register_SecurityAppSubstatus(SecurityAppSubstatus)
_ns_module._register_ShareWindowCommand(ShareWindowCommand)

AdaptiveCardBuilder = _ns_module.AdaptiveCardBuilder
FocusSession = _ns_module.FocusSession
FocusSessionManager = _ns_module.FocusSessionManager
SecurityAppManager = _ns_module.SecurityAppManager
ShareWindowCommandEventArgs = _ns_module.ShareWindowCommandEventArgs
ShareWindowCommandSource = _ns_module.ShareWindowCommandSource
TaskbarManager = _ns_module.TaskbarManager
IAdaptiveCard = _ns_module.IAdaptiveCard
IAdaptiveCardBuilderStatics = _ns_module.IAdaptiveCardBuilderStatics
