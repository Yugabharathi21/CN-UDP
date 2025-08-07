@echo off
title UDP Server - Intranet Version
color 0A
echo.
echo ================================================
echo           UDP SERVER - INTRANET VERSION
echo ================================================
echo.
echo Starting UDP Server...
echo Server will be accessible from any machine on the network
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

cd /d "%~dp0Server"
python udp_server.py

echo.
echo ================================================
echo Server has stopped.
echo ================================================
pause
