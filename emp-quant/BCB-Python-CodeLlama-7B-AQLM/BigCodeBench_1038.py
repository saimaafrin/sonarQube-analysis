from datetime import datetime
import json
BUFFER_SIZE = 1024
def task_func(client_socket):
    """
    Responds to a client's request by sending a JSON-formatted message containing
    the current server time and a greeting.

    Parameters:
    - client_socket (socket.socket): The client socket from which the request is received.

    Requirements:
    - datetime.datetime
    - json

    Returns:
    - None

    Example:
    >>> import socket
    >>> server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> server_socket.bind((SERVER_ADDRESS, 0))  # Bind to a free port
    >>> server_socket.bind((SERVER_ADDRESS, 8080))
    >>> server_socket.listen(1)
    >>> try:
    ...     client_socket, _ = server_socket.accept()
    ...     task_func(client_socket)
    ... finally:
    ...     server_socket.close()
    """
    # Receive the request from the client
    request = client_socket.recv(BUFFER_SIZE).decode()
    # Parse the request
    request_json = json.loads(request)
    # Send a response to the client
    response = json.dumps({
        "time": datetime.now().isoformat(),
        "greeting": "Hello, {}!".format(request_json["name"])
    })
    client_socket.send(response.encode())