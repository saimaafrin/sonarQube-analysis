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

    # Create a queue to store client sockets
    client_sockets = queue.Queue()

    # Create a queue to store received data
    received_data = queue.Queue()

    # Start the server
    print(f"Starting server on {server_address}:{server_port}")
    start_time = datetime.now()
    while True:
        # Check for incoming connections
        readable, _, _ = select.select([server_socket], [], [], 0.1)
        for sock in readable:
            # Accept the connection
            client_socket, client_address = server_socket.accept()
            client_sockets.put(client_socket)

            # Receive data from the client
            data = client_socket.recv(buffer_size)
            if data:
                received_data.put(data)

        # Check for received data
        readable, _, _ = select.select([received_data], [], [], 0.1)
        for data in readable:
            # Append the server's current time to the received data
            data += f"{datetime.now()}\n".encode()

            # Send the data back to the client
            client_socket = client_sockets.get()
            client_socket.sendall(data)

        # Check for client disconnections
        readable, _, _ = select.select([client_sockets], [], [], 0.1)
        for client_socket in readable:
            client_socket.close()
            client_sockets.get()

    # Stop the server
    end_time = datetime.now()
    run_time = end_time - start_time
    print(f"Server stopped after {run_time}")