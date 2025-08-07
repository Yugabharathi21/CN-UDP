@echo off
title UDP Client - Intranet Version
color 0B
echo.
echo ================================================
echo           UDP CLIENT - INTRANET VERSION
echo ================================================
echo.
echo Starting UDP Client...
echo You can connect to any UDP server on the network
echo.
echo Instructions:
echo 1. Choose server connection option
echo 2. Enter server IP address when prompted
echo 3. Type messages to send to server
echo 4. Type 'exit' to quit
echo ================================================
echo.

cd /d "%~dp0Client"
python udp_client.py

echo.
echo ================================================
echo Client has disconnected.
echo ================================================
pause
