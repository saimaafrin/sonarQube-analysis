
import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    try:
        # Create a socket and wrap it with SSL context
        context = ssl.create_default_context()
        conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)
        
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
        # Raise the SSL error
        raise e