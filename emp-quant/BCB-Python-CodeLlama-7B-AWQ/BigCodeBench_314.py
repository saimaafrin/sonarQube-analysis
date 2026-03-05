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
    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Create an HTTPS connection
        conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)

        # Make an HTTPS GET request
        conn.request("GET", path)

        # Get the response
        response = conn.getresponse()

        # Check the response status code
        if response.status != 200:
            raise Exception("Invalid response status code: {}".format(response.status))

        # Get the response body
        response_body = response.read()

        # Close the connection
        conn.close()

        # Return the response body
        return response_body.decode("utf-8")

    except ssl.SSLError as e:
        # Handle SSL handshake error
        raise Exception("SSL handshake error: {}".format(e))
SERVER_NAME = "example.com"
SERVER_PORT = 443
path = "/"