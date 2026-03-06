import socket
import ssl
import http.client
def task_func(SERVER_NAME, SERVER_PORT, path):
    """
    Makes an HTTPS GET request to a specified server and path, and retrieves the response.

    Parameters:
        SERVER_NAME (str): The name of the server to which the request is made.
        SERVER_PORT (int): The port number of the server to which the request is made.
        path (str): The path for the HTTP request.

    Returns:
        str: The response body from the server as a string.

    Raises:
        ssl.SSLError: If there is an SSL handshake error.

    Requirements:
    - socket
    - ssl
    - http.client

    Examples:
    >>> response = task_func('www.example.com', 443, '/path/to/request')
    >>> isinstance(response, str)
    True
    """
    # Create an SSL context
    context = ssl.create_default_context()

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    sock.connect((SERVER_NAME, SERVER_PORT))

    # Wrap the socket in an SSL socket
    ssl_sock = context.wrap_socket(sock, server_hostname=SERVER_NAME)

    # Create an HTTPS connection
    conn = http.client.HTTPSConnection(SERVER_NAME, port=SERVER_PORT,
                                       timeout=5,
                                       context=context)

    # Make the HTTPS request
    conn.request('GET', path)

    # Get the response
    response = conn.getresponse()

    # Get the response body
    response_body = response.read()

    # Close the connection
    conn.close()

    # Return the response body
    return response_body.decode('utf-8')