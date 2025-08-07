@echo off
echo UDP Client-Server Demo - Intranet Version
echo ==========================================
echo.
echo Choose an option:
echo 1. Start UDP Server
echo 2. Start UDP Client  
echo 3. Discover Servers on Network
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo Starting UDP Server...
    cd Server
    python udp_server.py
    pause
) else if "%choice%"=="2" (
    echo Starting UDP Client...
    cd Client
    python udp_client.py
    pause
) else if "%choice%"=="3" (
    echo Discovering servers on network...
    python network_discovery.py
    pause
) else if "%choice%"=="4" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto :start
)

:start
goto :eof
