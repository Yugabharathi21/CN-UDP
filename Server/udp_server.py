#!/usr/bin/env python3
"""
UDP Server - Receives messages from clients and sends replies
"""

import socket
import time

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Create a temporary socket to get local IP
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except:
        return "127.0.0.1"

def start_udp_server():
    # Server configuration
    SERVER_HOST = '0.0.0.0'    # Bind to all network interfaces (intranet accessible)
    SERVER_PORT = 12345        # Server port number
    
    # Get and display local IP address
    local_ip = get_local_ip()
    
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Bind the socket to the server address
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        print(f"UDP Server started on ALL INTERFACES:{SERVER_PORT}")
        print(f"Local IP Address: {local_ip}")
        print(f"Clients can connect using: {local_ip}:{SERVER_PORT}")
        print("Waiting for messages from clients...")
        print("-" * 60)
        
        while True:
            # Receive message from client
            message, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
            
            # Decode the received message
            received_message = message.decode('utf-8')
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[{current_time}] Received from {client_address}: {received_message}")
            
            # Prepare reply message
            reply_message = f"Server ({local_ip}) received: '{received_message}' at {current_time}"
            
            # Send reply back to client
            server_socket.sendto(reply_message.encode('utf-8'), client_address)
            print(f"[{current_time}] Sent reply to {client_address}")
            print("-" * 60)
            
            # Check for exit condition
            if received_message.lower() == 'exit':
                print("Exit command received. Shutting down server...")
                break
                
    except KeyboardInterrupt:
        print("\nServer interrupted by user. Shutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    start_udp_server()
