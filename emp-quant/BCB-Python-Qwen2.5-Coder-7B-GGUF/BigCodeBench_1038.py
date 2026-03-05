
from datetime import datetime
import json
SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    # Get the current server time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a greeting message
    greeting = "Hello, welcome to the server!"
    
    # Create a dictionary to hold the data to be sent
    data = {
        "current_time": current_time,
        "greeting": greeting
    }
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    
    # Send the JSON data to the client
    client_socket.sendall(json_data.encode())
    
    # Close the client socket
    client_socket.close()
    
    # Return None as per the requirement
    return None