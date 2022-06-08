// WARNING: Please don't edit this file. It was generated by C++/WinRT v2.0.220607.4

#pragma once
#ifndef WINRT_Windows_Phone_StartScreen_0_H
#define WINRT_Windows_Phone_StartScreen_0_H
WINRT_EXPORT namespace winrt::Windows::UI::Notifications
{
    struct BadgeUpdater;
    struct TileUpdater;
    struct ToastNotifier;
}
WINRT_EXPORT namespace winrt::Windows::Phone::StartScreen
{
    struct IDualSimTile;
    struct IDualSimTileStatics;
    struct IToastNotificationManagerStatics3;
    struct DualSimTile;
}
namespace winrt::impl
{
    template <> struct category<winrt::Windows::Phone::StartScreen::IDualSimTile>{ using type = interface_category; };
    template <> struct category<winrt::Windows::Phone::StartScreen::IDualSimTileStatics>{ using type = interface_category; };
    template <> struct category<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>{ using type = interface_category; };
    template <> struct category<winrt::Windows::Phone::StartScreen::DualSimTile>{ using type = class_category; };
    template <> inline constexpr auto& name_v<winrt::Windows::Phone::StartScreen::DualSimTile> = L"Windows.Phone.StartScreen.DualSimTile";
    template <> inline constexpr auto& name_v<winrt::Windows::Phone::StartScreen::IDualSimTile> = L"Windows.Phone.StartScreen.IDualSimTile";
    template <> inline constexpr auto& name_v<winrt::Windows::Phone::StartScreen::IDualSimTileStatics> = L"Windows.Phone.StartScreen.IDualSimTileStatics";
    template <> inline constexpr auto& name_v<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3> = L"Windows.Phone.StartScreen.IToastNotificationManagerStatics3";
    template <> inline constexpr guid guid_v<winrt::Windows::Phone::StartScreen::IDualSimTile>{ 0x143AB213,0xD05F,0x4041,{ 0xA1,0x8C,0x3E,0x3F,0xCB,0x75,0xB4,0x1E } }; // 143AB213-D05F-4041-A18C-3E3FCB75B41E
    template <> inline constexpr guid guid_v<winrt::Windows::Phone::StartScreen::IDualSimTileStatics>{ 0x50567C9E,0xC58F,0x4DC9,{ 0xB6,0xE8,0xFA,0x67,0x77,0xEE,0xEB,0x37 } }; // 50567C9E-C58F-4DC9-B6E8-FA6777EEEB37
    template <> inline constexpr guid guid_v<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>{ 0x2717F54B,0x50DF,0x4455,{ 0x8E,0x6E,0x41,0xE0,0xFC,0x8E,0x13,0xCE } }; // 2717F54B-50DF-4455-8E6E-41E0FC8E13CE
    template <> struct default_interface<winrt::Windows::Phone::StartScreen::DualSimTile>{ using type = winrt::Windows::Phone::StartScreen::IDualSimTile; };
    template <> struct abi<winrt::Windows::Phone::StartScreen::IDualSimTile>
    {
        struct __declspec(novtable) type : inspectable_abi
        {
            virtual int32_t __stdcall put_DisplayName(void*) noexcept = 0;
            virtual int32_t __stdcall get_DisplayName(void**) noexcept = 0;
            virtual int32_t __stdcall get_IsPinnedToStart(bool*) noexcept = 0;
            virtual int32_t __stdcall CreateAsync(void**) noexcept = 0;
            virtual int32_t __stdcall UpdateAsync(void**) noexcept = 0;
            virtual int32_t __stdcall DeleteAsync(void**) noexcept = 0;
        };
    };
    template <> struct abi<winrt::Windows::Phone::StartScreen::IDualSimTileStatics>
    {
        struct __declspec(novtable) type : inspectable_abi
        {
            virtual int32_t __stdcall GetTileForSim2(void**) noexcept = 0;
            virtual int32_t __stdcall UpdateDisplayNameForSim1Async(void*, void**) noexcept = 0;
            virtual int32_t __stdcall CreateTileUpdaterForSim1(void**) noexcept = 0;
            virtual int32_t __stdcall CreateTileUpdaterForSim2(void**) noexcept = 0;
            virtual int32_t __stdcall CreateBadgeUpdaterForSim1(void**) noexcept = 0;
            virtual int32_t __stdcall CreateBadgeUpdaterForSim2(void**) noexcept = 0;
            virtual int32_t __stdcall CreateToastNotifierForSim1(void**) noexcept = 0;
            virtual int32_t __stdcall CreateToastNotifierForSim2(void**) noexcept = 0;
        };
    };
    template <> struct abi<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>
    {
        struct __declspec(novtable) type : inspectable_abi
        {
            virtual int32_t __stdcall CreateToastNotifierForSecondaryTile(void*, void**) noexcept = 0;
        };
    };
    template <typename D>
    struct consume_Windows_Phone_StartScreen_IDualSimTile
    {
        auto DisplayName(param::hstring const& value) const;
        [[nodiscard]] auto DisplayName() const;
        [[nodiscard]] auto IsPinnedToStart() const;
        auto CreateAsync() const;
        auto UpdateAsync() const;
        auto DeleteAsync() const;
    };
    template <> struct consume<winrt::Windows::Phone::StartScreen::IDualSimTile>
    {
        template <typename D> using type = consume_Windows_Phone_StartScreen_IDualSimTile<D>;
    };
    template <typename D>
    struct consume_Windows_Phone_StartScreen_IDualSimTileStatics
    {
        auto GetTileForSim2() const;
        auto UpdateDisplayNameForSim1Async(param::hstring const& name) const;
        auto CreateTileUpdaterForSim1() const;
        auto CreateTileUpdaterForSim2() const;
        auto CreateBadgeUpdaterForSim1() const;
        auto CreateBadgeUpdaterForSim2() const;
        auto CreateToastNotifierForSim1() const;
        auto CreateToastNotifierForSim2() const;
    };
    template <> struct consume<winrt::Windows::Phone::StartScreen::IDualSimTileStatics>
    {
        template <typename D> using type = consume_Windows_Phone_StartScreen_IDualSimTileStatics<D>;
    };
    template <typename D>
    struct consume_Windows_Phone_StartScreen_IToastNotificationManagerStatics3
    {
        auto CreateToastNotifierForSecondaryTile(param::hstring const& tileId) const;
    };
    template <> struct consume<winrt::Windows::Phone::StartScreen::IToastNotificationManagerStatics3>
    {
        template <typename D> using type = consume_Windows_Phone_StartScreen_IToastNotificationManagerStatics3<D>;
    };
}
#endif