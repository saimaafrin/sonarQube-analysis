
from datetime import datetime
import json
SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    # Get the current server time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a greeting message
    greeting = "Hello, client!"
    
    # Create a JSON-formatted message
    message = {
        "server_time": current_time,
        "greeting": greeting
    }
    
    # Convert the message to a JSON string
    json_message = json.dumps(message)
    
    # Send the JSON message to the client
    client_socket.sendall(json_message.encode())
    
    # Close the client socket
    client_socket.close()
    
    return None