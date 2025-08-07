@echo off
title UDP Demo - Main Menu
color 0F

:main_menu
cls
echo.
echo ================================================
echo        UDP CLIENT-SERVER DEMO - MAIN MENU
echo ================================================
echo.
echo Choose an option:
echo.
echo 1. Start UDP Server
echo 2. Start UDP Client  
echo 3. Find Servers on Network
echo 4. View README Instructions
echo 5. Exit
echo.
echo ================================================
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Starting UDP Server...
    start "" "%~dp0start_server.bat"
    echo Server started in new window.
    echo.
    pause
    goto main_menu
) else if "%choice%"=="2" (
    echo.
    echo Starting UDP Client...
    start "" "%~dp0start_client.bat"
    echo Client started in new window.
    echo.
    pause
    goto main_menu
) else if "%choice%"=="3" (
    echo.
    echo Starting Network Discovery...
    start "" "%~dp0find_servers.bat"
    echo Network scanner started in new window.
    echo.
    pause
    goto main_menu
) else if "%choice%"=="4" (
    echo.
    echo Opening README file...
    start "" notepad.exe "%~dp0README.md"
    goto main_menu
) else if "%choice%"=="5" (
    echo.
    echo Goodbye!
    exit
) else (
    echo.
    echo Invalid choice. Please try again.
    pause
    goto main_menu
)
