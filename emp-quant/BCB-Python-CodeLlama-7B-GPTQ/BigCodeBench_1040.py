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
    server_socket.listen()

    # Create a queue to store client sockets
    client_sockets = queue.Queue()

    # Start the server
    print(f"Starting server on {server_address}:{server_port}")
    start_time = datetime.now()
    while (datetime.now() - start_time) < timedelta(seconds=run_duration):
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        client_sockets.put(client_socket)

        # Handle client data
        while True:
            try:
                data = client_socket.recv(buffer_size)
                if not data:
                    break
                data = data.decode("utf-8")
                data += f" {datetime.now().strftime('%H:%M:%S')}"
                client_socket.sendall(data.encode("utf-8"))
            except socket.error as e:
                print(f"Error: {e}")
                client_socket.close()
                break

    # Close the server
    print(f"Server stopped after {run_duration} seconds")
    server_socket.close()