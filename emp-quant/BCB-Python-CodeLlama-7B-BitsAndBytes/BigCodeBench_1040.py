
import socket
import select
import queue
from datetime import datetime, timedelta

def task_func(
    server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5
):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_address, server_port))
    server_socket.listen(1)

    # Set up the selectors
    selector = select.DefaultSelector()
    selector.register(server_socket, select.EPOLLIN)

    # Set up the buffer
    buffer = bytearray(buffer_size)

    # Set up the run duration
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=run_duration)

    # Run the server
    while datetime.now() < end_time:
        # Wait for a connection
        ready_sockets = selector.select(0.1)
        if server_socket in ready_sockets:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            selector.register(client_socket, select.EPOLLIN)

            # Read data from the client
            data = client_socket.recv(buffer_size)
            if data:
                # Append the current time to the data
                data += f"{datetime.now():%Y-%m-%d %H:%M:%S}".encode()

                # Send the data back to the client
                client_socket.sendall(data)

                # Close the client socket
                client_socket.close()

    # Print the status message
    print(f"Server ran for {run_duration} seconds")

    # Close the server socket
    server_socket.close()