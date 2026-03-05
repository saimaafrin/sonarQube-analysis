
import socket
import select
import queue
from datetime import datetime, timedelta

def task_func(
    server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5
):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)

    # Set up the select loop
    read_sockets = [server_socket]
    write_sockets = []
    error_sockets = []
    timeout = 1

    # Set up the buffer
    buffer = b""

    # Set up the start time
    start_time = datetime.now()

    # Run the server
    while True:
        # Check for any incoming connections
        readable, writable, exceptional = select.select(read_sockets, write_sockets, error_sockets, timeout)

        # Handle incoming connections
        for sock in readable:
            if sock is server_socket:
                # Accept the connection
                client_socket, client_address = server_socket.accept()
                read_sockets.append(client_socket)
                write_sockets.append(client_socket)
                error_sockets.append(client_socket)
            else:
                # Read data from the client
                data = sock.recv(buffer_size)
                if data:
                    # Append the current time to the data
                    data += f" {datetime.now():%Y-%m-%d %H:%M:%S}\n".encode()
                    # Write the data back to the client
                    sock.sendall(data)
                else:
                    # Close the connection
                    sock.close()
                    read_sockets.remove(sock)
                    write_sockets.remove(sock)
                    error_sockets.remove(sock)

        # Handle exceptions
        for sock in exceptional:
            sock.close()
            read_sockets.remove(sock)
            write_sockets.remove(sock)
            error_sockets.remove(sock)

    # Calculate the run duration
    end_time = datetime.now()
    run_duration = end_time - start_time

    # Output the status message
    print(f"Server running for {run_duration.total_seconds()} seconds")