
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
        sock.connect((SERVER_NAME, SERVER_PORT))
        
        # Wrap the socket with SSL context
        secure_sock = context.wrap_socket(sock, server_hostname=SERVER_NAME)
        
        # Create an HTTP connection object
        conn = http.client.HTTPSConnection(SERVER_NAME, server_hostname=SERVER_NAME, context=context)
        
        # Make the GET request
        conn.request("GET", path)
        
        # Get the response
        response = conn.getresponse()
        
        # Read the response body
        response_body = response.read().decode('utf-8')
        
        # Close the connection
        conn.close()
        
        return response_body
    
    except ssl.SSLError as e:
        raise e