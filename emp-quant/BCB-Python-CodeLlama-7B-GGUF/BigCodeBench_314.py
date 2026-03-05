
import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    # Create an SSL context
    context = ssl.create_default_context()

    # Create an HTTPS connection
    conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)

    # Make an HTTPS GET request
    conn.request("GET", path)

    # Get the response
    response = conn.getresponse()

    # Check for an SSL handshake error
    if response.status == 400 and response.reason == "Bad Request":
        raise ssl.SSLError("SSL handshake error")

    # Get the response body as a string
    response_body = response.read().decode("utf-8")

    # Close the connection
    conn.close()

    return response_body