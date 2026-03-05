
from datetime import datetime
import json
SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    # Get the current server time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a greeting message
    greeting = "Hello, welcome to the server!"
    
    # Create a dictionary to hold the response data
    response_data = {
        "time": current_time,
        "greeting": greeting
    }
    
    # Convert the dictionary to a JSON-formatted string
    response_json = json.dumps(response_data)
    
    # Send the JSON response to the client
    client_socket.sendall(response_json.encode())
    
    # Close the client socket
    client_socket.close()
    
    # Return None as per the requirement
    return None