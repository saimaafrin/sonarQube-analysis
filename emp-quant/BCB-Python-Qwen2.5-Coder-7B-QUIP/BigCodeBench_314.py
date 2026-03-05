
import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    # Create a socket object
    conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))
    
    # Make a GET request
    conn.request("GET", path)
    
    # Get the response
    response = conn.getresponse()
    
    # Read the response body
    body = response.read().decode('utf-8')
    
    # Close the connection
    conn.close()
    
    # Return the response body
    return body