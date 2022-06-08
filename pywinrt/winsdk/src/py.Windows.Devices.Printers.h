// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Graphics.Printing.h")
#include "py.Windows.Graphics.Printing.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Devices.Printers.h>

namespace py::proj::Windows::Devices::Printers
{}

namespace py::impl::Windows::Devices::Printers
{}

namespace py::wrapper::Windows::Devices::Printers
{
    using IppAttributeError = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppAttributeError>;
    using IppAttributeValue = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppAttributeValue>;
    using IppIntegerRange = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppIntegerRange>;
    using IppPrintDevice = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppPrintDevice>;
    using IppResolution = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppResolution>;
    using IppSetAttributesResult = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppSetAttributesResult>;
    using IppTextWithLanguage = py::winrt_wrapper<winrt::Windows::Devices::Printers::IppTextWithLanguage>;
    using PageConfigurationSettings = py::winrt_wrapper<winrt::Windows::Devices::Printers::PageConfigurationSettings>;
    using PdlPassthroughProvider = py::winrt_wrapper<winrt::Windows::Devices::Printers::PdlPassthroughProvider>;
    using PdlPassthroughTarget = py::winrt_wrapper<winrt::Windows::Devices::Printers::PdlPassthroughTarget>;
    using Print3DDevice = py::winrt_wrapper<winrt::Windows::Devices::Printers::Print3DDevice>;
    using PrintSchema = py::winrt_wrapper<winrt::Windows::Devices::Printers::PrintSchema>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::Devices::Printers::IppAttributeErrorReason>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Devices::Printers::IppAttributeValueKind>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Devices::Printers::IppResolutionUnit>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Devices::Printers::PageConfigurationSource>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppAttributeError>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppAttributeValue>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppIntegerRange>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppPrintDevice>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppResolution>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppSetAttributesResult>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::IppTextWithLanguage>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::PageConfigurationSettings>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::PdlPassthroughProvider>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::PdlPassthroughTarget>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::Print3DDevice>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Printers::PrintSchema>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}
