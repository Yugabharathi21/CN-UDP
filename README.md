# UDP Client-Server Communication Demo - Intranet Version

This project demonstrates UDP (User Datagram Protocol) communication between clients and servers across a college intranet network, allowing any connected system to participate.

## Files Structure
```
Computer networks/
├── Server/
│   └── udp_server.py    # UDP Server (intranet accessible)
├── Client/
│   └── udp_client.py    # UDP Client (connects to any server IP)
├── network_discovery.py # Network scanner to find active servers
├── run_demo.bat        # Windows batch script for easy execution
└── README.md           # This file
```

## Features

### UDP Server (`udp_server.py`)
- **Intranet Accessible**: Binds to all network interfaces (0.0.0.0)
- **Multi-Client Support**: Handles multiple clients simultaneously
- **IP Discovery**: Displays local IP address for client connections
- **Real-time Communication**: Instant message exchange with timestamps
- **Network-wide Visibility**: Can be accessed from any system on the intranet

### UDP Client (`udp_client.py`)
- **Flexible Connection**: Can connect to any server IP on the network
- **Interactive IP Selection**: Choose server IP via menu or manual entry
- **Network Awareness**: Displays local and target IP addresses
- **Error Handling**: Robust connection and timeout management
- **Cross-machine Communication**: Works across different systems

### Network Discovery (`network_discovery.py`)
- **Server Detection**: Automatically finds active UDP servers on the network
- **Network Scanning**: Scans the entire subnet for available servers
- **Parallel Processing**: Fast multi-threaded network scanning
- **Connection Testing**: Verifies server availability before listing

## How to Run on College Intranet

### Method 1: Using the Batch Script (Windows)
Simply double-click `run_demo.bat` and choose from the menu options.

### Method 2: Manual Setup

#### Step 1: Start a Server (on any machine)
1. Open PowerShell/Command Prompt
2. Navigate to the project directory:
   ```powershell
   cd "d:\Computer networks\Server"
   ```
3. Run the server:
   ```powershell
   python udp_server.py
   ```
4. **Note the displayed IP address** - other students will use this to connect

#### Step 2: Find Available Servers (optional)
1. On any machine, navigate to the project directory:
   ```powershell
   cd "d:\Computer networks"
   ```
2. Run the network discovery:
   ```powershell
   python network_discovery.py
   ```
3. This will show all available servers on the network

#### Step 3: Connect Clients (from any machine)
1. Navigate to the Client directory:
   ```powershell
   cd "d:\Computer networks\Client"
   ```
2. Run the client:
   ```powershell
   python udp_client.py
   ```
3. Choose how to connect:
   - **Option 1**: Enter the server's IP address manually
   - **Option 2**: Use localhost (if server is on same machine)
   - **Option 3**: Auto-detect (uses your local IP)

## Example Usage on Intranet

### Server Output:
```
UDP Server started on ALL INTERFACES:12345
Local IP Address: 192.168.1.105
Clients can connect using: 192.168.1.105:12345
Waiting for messages from clients...
------------------------------------------------------------
[2025-08-07 14:30:15] Received from ('192.168.1.110', 54321): Hello from Computer Lab PC-15!
[2025-08-07 14:30:15] Sent reply to ('192.168.1.110', 54321)
------------------------------------------------------------
```

### Client Output:
```
UDP Client - Intranet Version
========================================
Server IP Options:
1. Enter specific IP address
2. Use localhost (127.0.0.1)
3. Auto-detect (use local network IP)
Choose option (1-3): 1
Enter server IP address: 192.168.1.105
Client Local IP: 192.168.1.110
Connecting to server at 192.168.1.105:12345
Type 'exit' to quit the client
------------------------------------------------------------
Enter message to send to server: Hello from Computer Lab PC-15!
[2025-08-07 14:30:15] Sent: Hello from Computer Lab PC-15!
[2025-08-07 14:30:15] Server reply: Server (192.168.1.105) received: 'Hello from Computer Lab PC-15!' at 2025-08-07 14:30:15
------------------------------------------------------------
```

### Network Discovery Output:
```
UDP Server Discovery Tool
========================================
Local IP: 192.168.1.110
Scanning network: 192.168.1.0/24

Scanning network 192.168.1.0/24 for UDP servers on port 12345...
This may take a few moments...
------------------------------------------------------------
✓ Found server at 192.168.1.105:12345
✓ Found server at 192.168.1.120:12345
------------------------------------------------------------
Found 2 UDP server(s):
1. 192.168.1.105:12345
   Response: Server (192.168.1.105) received: 'DISCOVERY_PING'...
2. 192.168.1.120:12345
   Response: Server (192.168.1.120) received: 'DISCOVERY_PING'...

You can use any of these IP addresses in your UDP client!
```

## Intranet Setup Tips

### For Server Hosts:
1. **Share your IP**: Tell other students your server's IP address
2. **Firewall**: Ensure Windows Firewall allows Python through
3. **Port 12345**: Make sure this port isn't blocked by network policies
4. **Keep Running**: Leave the server running for others to connect

### For Clients:
1. **Get Server IP**: Ask the server host for their IP address
2. **Use Discovery**: Run `network_discovery.py` to find available servers
3. **Multiple Servers**: You can connect to different servers
4. **Same Network**: Ensure you're on the same intranet/WiFi network

### Network Requirements:
- All systems must be on the same subnet (common in college labs)
- Port 12345 should be accessible (not blocked by firewall)
- Python 3.x installed on all participating systems

## Troubleshooting

### "No servers found" during discovery:
- Check if server is actually running
- Verify you're on the same network
- Try manually entering the server IP

### "Connection timeout" in client:
- Server might be down or unreachable
- Check firewall settings on server machine
- Verify the IP address is correct

### Permission errors:
- Run as administrator if needed
- Check Windows Firewall settings

## Requirements

- Python 3.x
- No additional packages required (uses built-in `socket` module)
