@echo off
title Network Discovery - Find UDP Servers
color 0E
echo.
echo ================================================
echo        NETWORK DISCOVERY - FIND UDP SERVERS
echo ================================================
echo.
echo This tool will scan your network to find active UDP servers
echo Please wait while scanning...
echo.
echo ================================================
echo.

python network_discovery.py

echo.
echo ================================================
echo Network scan completed.
echo ================================================
pause
