#!/usr/bin/env python3
"""
Network Discovery Tool - Find UDP servers on the intranet
"""

import socket
import threading
import time
import ipaddress

def get_local_network():
    """Get the local network range"""
    try:
        # Get local IP
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        
        # Assume /24 subnet (common in college networks)
        network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
        return network, local_ip
    except:
        return None, "127.0.0.1"

def check_server(ip, port, timeout=2):
    """Check if a UDP server is running on given IP:port"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(timeout)
        
        # Send a discovery message
        test_message = "DISCOVERY_PING"
        client_socket.sendto(test_message.encode('utf-8'), (str(ip), port))
        
        # Try to receive response
        reply, server_address = client_socket.recvfrom(1024)
        client_socket.close()
        
        return True, reply.decode('utf-8')
    except:
        if 'client_socket' in locals():
            client_socket.close()
        return False, None

def scan_network_for_servers(network, port=12345):
    """Scan the network for UDP servers"""
    print(f"Scanning network {network} for UDP servers on port {port}...")
    print("This may take a few moments...")
    print("-" * 60)
    
    found_servers = []
    threads = []
    lock = threading.Lock()
    
    def scan_ip(ip):
        is_server, response = check_server(ip, port)
        if is_server:
            with lock:
                found_servers.append((str(ip), response))
                print(f"✓ Found server at {ip}:{port}")
    
    # Create threads for parallel scanning
    for ip in network.hosts():
        if len(threads) >= 50:  # Limit concurrent threads
            for t in threads:
                t.join()
            threads = []
        
        thread = threading.Thread(target=scan_ip, args=(ip,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return found_servers

def main():
    print("UDP Server Discovery Tool")
    print("=" * 40)
    
    # Get local network information
    network, local_ip = get_local_network()
    
    if network is None:
        print("Could not determine local network. Using localhost.")
        network = ipaddress.IPv4Network("127.0.0.1/32")
    
    print(f"Local IP: {local_ip}")
    print(f"Scanning network: {network}")
    print()
    
    # Scan for servers
    servers = scan_network_for_servers(network)
    
    print("-" * 60)
    if servers:
        print(f"Found {len(servers)} UDP server(s):")
        for i, (ip, response) in enumerate(servers, 1):
            print(f"{i}. {ip}:12345")
            print(f"   Response: {response[:50]}...")
        
        print("\nYou can use any of these IP addresses in your UDP client!")
    else:
        print("No UDP servers found on the network.")
        print("Make sure the server is running and accessible.")
    
    print("\nTo connect manually, use the UDP client with the server IP address.")

if __name__ == "__main__":
    main()
