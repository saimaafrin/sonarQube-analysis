
import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    # Create an SSL context
    context = ssl.create_default_context()

    # Create an HTTPS connection
    conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)

    # Make the GET request
    conn.request("GET", path)

    # Get the response
    response = conn.getresponse()

    # Check for SSL handshake errors
    if response.status == 400:
        raise ssl.SSLError("SSL handshake error")

    # Read the response body
    response_body = response.read()

    # Close the connection
    conn.close()

    # Return the response body as a string
    return response_body.decode("utf-8")