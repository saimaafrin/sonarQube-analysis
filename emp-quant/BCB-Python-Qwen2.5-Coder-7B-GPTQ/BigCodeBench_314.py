import socket
import ssl
import http.client
def task_func(SERVER_NAME, SERVER_PORT, path):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Create an SSL context
        context = ssl.create_default_context()
        
        # Connect to the server
        with context.wrap_socket(sock, server_hostname=SERVER_NAME) as ssock:
            # Create an HTTP connection using the SSL socket
            conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, socket=ssock)
            
            # Make a GET request
            conn.request("GET", path)
            
            # Get the response
            response = conn.getresponse()
            
            # Read the response body
            response_body = response.read()
            
            # Close the connection
            conn.close()
            
            # Return the response body as a string
            return response_body.decode('utf-8')
    except ssl.SSLError as e:
        # Raise the SSL error if it occurs
        raise e