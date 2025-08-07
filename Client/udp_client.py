#!/usr/bin/env python3
"""
UDP Client - Sends messages to server and receives replies
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

def get_server_ip():
    """Get server IP from user input"""
    print("Server IP Options:")
    print("1. Enter specific IP address")
    print("2. Use localhost (127.0.0.1)")
    print("3. Auto-detect (use local network IP)")
    
    choice = input("Choose option (1-3): ").strip()
    
    if choice == "1":
        server_ip = input("Enter server IP address: ").strip()
        return server_ip
    elif choice == "2":
        return "127.0.0.1"
    elif choice == "3":
        local_ip = get_local_ip()
        return local_ip
    else:
        print("Invalid choice. Using localhost.")
        return "127.0.0.1"

def start_udp_client():
    # Get server configuration from user
    print("UDP Client - Intranet Version")
    print("=" * 40)
    SERVER_HOST = get_server_ip()
    SERVER_PORT = 12345        # Server port number
    
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        print(f"Client Local IP: {get_local_ip()}")
        print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}")
        print("Type 'exit' to quit the client")
        print("-" * 60)
        
        while True:
            # Get message from user
            message = input("Enter message to send to server: ")
            
            if not message:
                print("Empty message. Please enter a valid message.")
                continue
            
            # Send message to server
            try:
                client_socket.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{current_time}] Sent: {message}")
            except OSError as e:
                if hasattr(e, 'winerror') and e.winerror == 10054:
                    print(f"[{current_time}] Server connection lost (Error 10054)")
                    print("The server may have been closed or is unreachable.")
                    break
                else:
                    print(f"[{current_time}] Error sending message: {e}")
                    continue
            
            # Receive reply from server
            try:
                client_socket.settimeout(5.0)  # 5 second timeout
                reply, server_address = client_socket.recvfrom(1024)  # Buffer size of 1024 bytes
                reply_message = reply.decode('utf-8')
                print(f"[{current_time}] Server reply: {reply_message}")
                print("-" * 60)
                
                # Check for exit condition
                if message.lower() == 'exit':
                    print("Exit command sent. Closing client...")
                    break
                    
            except socket.timeout:
                print("No response from server (timeout)")
                print("Server might be busy or unreachable. Try again.")
            except OSError as e:
                if hasattr(e, 'winerror') and e.winerror == 10054:
                    print("Server closed the connection (Error 10054)")
                    print("The server may have shut down.")
                    break
                else:
                    print(f"Error receiving reply: {e}")
            except UnicodeDecodeError:
                print("Received invalid data from server")
            except Exception as e:
                print(f"Unexpected error: {e}")
                
    except KeyboardInterrupt:
        print("\nClient interrupted by user. Shutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()
        print("Client socket closed.")

def send_single_message():
    """Alternative function to send a single message (for testing)"""
    SERVER_HOST = input("Enter server IP address: ").strip() or "127.0.0.1"
    SERVER_PORT = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        message = "Hello from UDP Client!"
        client_socket.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
        print(f"Sent: {message}")
        
        reply, server_address = client_socket.recvfrom(1024)
        print(f"Server reply: {reply.decode('utf-8')}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    # Run interactive client
    start_udp_client()
    
    # Uncomment the line below to test with a single message instead
    # send_single_message()
