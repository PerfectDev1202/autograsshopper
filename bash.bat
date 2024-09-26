@echo off
:: Set the path to the .exe file
set EXE_PATH=C:\\Program Files\\Grasshopper\\Grasshopper.exe

:: Set the path where you want to place the shortcut
set SHORTCUT_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Grasshopper.lnk

:: Set the hotkey
set HOTKEY=Ctrl+Alt+Q

:: Create a PowerShell script that will generate the shortcut and assign the hotkey
powershell -Command ^
    $WshShell = New-Object -ComObject WScript.Shell; ^
    $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); ^
    $Shortcut.TargetPath = '%EXE_PATH%'; ^
    $Shortcut.Hotkey = '%HOTKEY%'; ^
    $Shortcut.Save();

pip install pyautogui numpy pywin32 opencv-python
