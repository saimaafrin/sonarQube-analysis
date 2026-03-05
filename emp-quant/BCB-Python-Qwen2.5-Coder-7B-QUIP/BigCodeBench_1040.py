
import socket
import select
import queue
from datetime import datetime, timedelta

def task_func(
    server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5
):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)
    server_socket.setblocking(False)

    # Create a queue for non-blocking I/O
    input_queue = queue.Queue()

    # Start the server
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=run_duration)

    while datetime.now() < end_time:
        # Check for incoming connections
        readable, _, _ = select.select([server_socket], [], [], 0.1)
        if server_socket in readable:
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(False)
            input_queue.put(client_socket)

        # Process data from clients
        while not input_queue.empty():
            client_socket = input_queue.get()
            try:
                data = client_socket.recv(buffer_size)
                if data:
                    # Append the current time to the received data
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    data += b" " + current_time.encode()
                    client_socket.sendall(data)
                else:
                    # Client has disconnected
                    client_socket.close()
            except socket.error as e:
                # Handle socket errors
                print(f"Socket error: {e}")
                client_socket.close()

    # Clean up
    server_socket.close()
    print(f"Server ran for {run_duration} seconds")