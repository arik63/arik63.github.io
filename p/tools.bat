@echo off
:menu
cls
echo ===================================
echo            Menu Options
echo ===================================
echo 1) Computer Management
echo 2) Control Panel
echo 3) Device Manager
echo 4) Download AnyDesk
echo 5) Download TeamViewer
echo 6) Firewall Settings
echo 7) IPCONFIG
echo 8) IPCONFIG /ALL
echo 9) IPv4 Address
echo 10) My Computer
echo 11) Network Adapter Settings
echo 12) Notepad
echo 13) Ping 8.8.8.8
echo 14) Ping -t 8.8.8.8
echo 15) Print Management
echo 16) Printers
echo 17) Recycle Bin
echo 18) Registry Editor
echo 19) Remove Programs
echo 20) Restart Explorer
echo 21) Sign Out
echo 22) Turn Windows Features On or Off
echo 23) whoami
echo 24) whoami /user
echo 25) Show Desktop
echo 26) See Drives Space (Formatted)
echo ===================================
echo By arik63.github.io
echo ===================================
set /p choice="Enter your choice (1-26): "

if "%choice%"=="1" goto computer_management
if "%choice%"=="2" goto start_control
if "%choice%"=="3" goto device_manager
if "%choice%"=="4" goto download_anydesk
if "%choice%"=="5" goto download_teamviewer
if "%choice%"=="6" goto firewall_settings
if "%choice%"=="7" goto ipconfig
if "%choice%"=="8" goto ipconfig_all
if "%choice%"=="9" goto ipv4_address
if "%choice%"=="10" goto my_computer
if "%choice%"=="11" goto network_adapter
if "%choice%"=="12" goto notepad
if "%choice%"=="13" goto ping_8_8_8_8
if "%choice%"=="14" goto ping_t_8_8_8_8
if "%choice%"=="15" goto print_management
if "%choice%"=="16" goto printers
if "%choice%"=="17" goto recycle_bin
if "%choice%"=="18" goto registry_editor
if "%choice%"=="19" goto remove_programs
if "%choice%"=="20" goto restart_explorer
if "%choice%"=="21" goto sign_out
if "%choice%"=="22" goto windows_features
if "%choice%"=="23" goto whoami
if "%choice%"=="24" goto whoami_user
if "%choice%"=="25" goto show_desktop
if "%choice%"=="26" goto see_drives_space
echo Invalid choice. Please try again.
pause
goto menu

:computer_management
start compmgmt.msc
goto menu

:start_control
start control
goto menu

:device_manager
start devmgmt.msc
goto menu

:download_anydesk
start "" "https://download.anydesk.com/AnyDesk.exe"
goto menu

:download_teamviewer
start "" "https://150.co.il/downloads/TeamViewerQS1"
goto menu

:firewall_settings
start firewall.cpl
goto menu

:ipconfig
ipconfig
pause
goto menu

:ipconfig_all
ipconfig /all
pause
goto menu

:ipv4_address
for /f "tokens=14" %%i in ('ipconfig ^| findstr /R /C:"IPv4 Address"') do @echo %%i
pause
goto menu

:my_computer
start explorer.exe
goto menu

:network_adapter
start ncpa.cpl
goto menu

:notepad
start notepad.exe
goto menu

:ping_8_8_8_8
ping 8.8.8.8
pause
goto menu

:ping_t_8_8_8_8
ping -t 8.8.8.8
pause
goto menu

:print_management
start printmanagement.msc
goto menu

:printers
start shell:PrintersFolder
goto menu

:recycle_bin
start shell:RecycleBinFolder
goto menu

:registry_editor
start regedit
goto menu

:remove_programs
start appwiz.cpl
goto menu

:restart_explorer
echo Closing Explorer...
taskkill /f /im explorer.exe
echo Starting Explorer...
start explorer.exe
pause
goto menu

:sign_out
echo Signing out...
shutdown /l
exit

:windows_features
start optionalfeatures.exe
goto menu

:whoami
whoami
pause
goto menu

:whoami_user
whoami /user
pause
goto menu

:show_desktop
powershell -command "(New-Object -ComObject shell.application).ToggleDesktop()"
goto menu

:see_drives_space
for /f "tokens=1-3" %%a in ('wmic logicaldisk get FreeSpace^,Name^,Size ^| findstr /i /v "Name"') do (
    echo %%b free=%%c size=%%a
    echo.
)
pause
goto menu
