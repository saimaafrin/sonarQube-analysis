
import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    # Create an SSL context
    context = ssl.create_default_context()

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    sock.connect((SERVER_NAME, SERVER_PORT))

    # Create an SSL object
    ssl_sock = context.wrap(sock)

    # Send the GET request
    request = "GET " + path + " HTTP/1.0\r\n\r\n"
    ssl_sock.write(request.encode())

    # Read the response
    response = ssl_sock.read()

    # Close the socket
    ssl_sock.close()

    # Return the response
    return response