# Windows Error 10054 Troubleshooting Guide

## What is Error 10054?
Windows Error 10054 ("Connection reset by peer") occurs when:
- A client disconnects abruptly (closes window, Ctrl+C)
- Network connection is lost
- Firewall blocks the connection
- Server tries to send data to a disconnected client

## Quick Fixes Applied:

### 1. Server Improvements:
- Added error handling for disconnected clients
- Server continues running even if clients disconnect
- Better socket options to prevent Windows-specific issues

### 2. Client Improvements:
- Added timeout handling (5 seconds)
- Graceful error messages
- Automatic reconnection capability

## If You Still Get Error 10054:

### For Server:
```powershell
# Run as Administrator (if needed)
Right-click PowerShell → "Run as Administrator"
cd "d:\Computer networks\Server"
python udp_server.py
```

### For Client:
1. **Make sure server is running first**
2. **Use correct IP address**
3. **Check Windows Firewall**:
   - Go to Windows Firewall settings
   - Allow Python through firewall
   - Or temporarily disable firewall for testing

### Network Troubleshooting:
```powershell
# Test if server IP is reachable
ping 192.168.1.105

# Check if port is open (from client machine)
telnet 192.168.1.105 12345
```

### Alternative Port:
If port 12345 is blocked, change it in both files:
- Server: `SERVER_PORT = 8888`
- Client: `SERVER_PORT = 8888`

## Common Scenarios:

### ✅ Normal Operation:
```
Client connects → Sends message → Gets reply → Continues
```

### ⚠️ Error 10054 Handled:
```
Client connects → Sends message → Client crashes/disconnects
Server: "Client disconnected unexpectedly (Error 10054)"
Server: "Continuing to listen for other clients..."
```

### 🔄 Auto-Recovery:
- Server keeps running even if clients disconnect
- Clients can reconnect without restarting server
- Multiple clients can connect simultaneously

The updated code should now handle Error 10054 gracefully without crashing!
