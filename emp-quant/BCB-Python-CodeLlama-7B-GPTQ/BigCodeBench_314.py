import socket
import ssl
import http.client
def task_func(SERVER_NAME, SERVER_PORT, path):
    """
    Makes an HTTPS GET request to a specified server and path, and retrieves the response.
    The function should raise the exception for: ssl.SSLError: If there is an SSL handshake error.
    The function should output with:
        str: The response body from the server as a string.
    """
    # Create an SSL context
    context = ssl.create_default_context()

    # Create an HTTPS connection
    conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)

    # Make an HTTPS GET request
    conn.request("GET", path)

    # Get the response
    response = conn.getresponse()

    # Check if the response is an error
    if response.status != 200:
        raise Exception("Error: {}".format(response.status))

    # Get the response body
    data = response.read()

    # Close the connection
    conn.close()

    # Return the response body as a string
    return data.decode("utf-8")
SERVER_NAME = "example.com"
SERVER_PORT = 443
path = "/"