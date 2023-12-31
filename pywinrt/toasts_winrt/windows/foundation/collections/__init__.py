# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.10

import enum

import toasts_winrt.system

_ns_module = toasts_winrt.system._import_ns_module("Windows.Foundation.Collections")

try:
    import toasts_winrt.windows.foundation
except ImportError:
    pass

class CollectionChange(enum.IntEnum):
    RESET = 0
    ITEM_INSERTED = 1
    ITEM_REMOVED = 2
    ITEM_CHANGED = 3

_ns_module._register_CollectionChange(CollectionChange)

PropertySet = _ns_module.PropertySet
toasts_winrt.system._mixin_mutable_mapping(PropertySet)
StringMap = _ns_module.StringMap
toasts_winrt.system._mixin_mutable_mapping(StringMap)
ValueSet = _ns_module.ValueSet
toasts_winrt.system._mixin_mutable_mapping(ValueSet)
IIterable = _ns_module.IIterable
IIterator = _ns_module.IIterator
IKeyValuePair = _ns_module.IKeyValuePair
IMapChangedEventArgs = _ns_module.IMapChangedEventArgs
IMapView = _ns_module.IMapView
toasts_winrt.system._mixin_mapping(IMapView)
IMap = _ns_module.IMap
toasts_winrt.system._mixin_mutable_mapping(IMap)
IObservableMap = _ns_module.IObservableMap
toasts_winrt.system._mixin_mutable_mapping(IObservableMap)
IObservableVector = _ns_module.IObservableVector
toasts_winrt.system._mixin_mutable_sequence(IObservableVector)
IPropertySet = _ns_module.IPropertySet
toasts_winrt.system._mixin_mutable_mapping(IPropertySet)
IVectorChangedEventArgs = _ns_module.IVectorChangedEventArgs
IVectorView = _ns_module.IVectorView
toasts_winrt.system._mixin_sequence(IVectorView)
IVector = _ns_module.IVector
toasts_winrt.system._mixin_mutable_sequence(IVector)
