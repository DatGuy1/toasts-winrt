// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Phone.UI.Input.h>

namespace py::proj::Windows::Phone::UI::Input
{}

namespace py::impl::Windows::Phone::UI::Input
{}

namespace py::wrapper::Windows::Phone::UI::Input
{
    using BackPressedEventArgs = py::winrt_wrapper<winrt::Windows::Phone::UI::Input::BackPressedEventArgs>;
    using CameraEventArgs = py::winrt_wrapper<winrt::Windows::Phone::UI::Input::CameraEventArgs>;
    using HardwareButtons = py::winrt_wrapper<winrt::Windows::Phone::UI::Input::HardwareButtons>;
}

namespace py
{

    template<>
    struct winrt_type<winrt::Windows::Phone::UI::Input::BackPressedEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Phone::UI::Input::CameraEventArgs>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Phone::UI::Input::HardwareButtons>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}