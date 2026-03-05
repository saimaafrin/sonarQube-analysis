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
    server_socket.listen(1)

    # Set up the queue for the client connections
    client_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses
    address_queue = queue.Queue()

    # Set up the queue for the client sockets
    socket_queue = queue.Queue()

    # Set up the queue for the client data
    data_queue = queue.Queue()

    # Set up the queue for the client addresses