
from datetime import datetime
import json

SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    # Get the current time
    current_time = datetime.now()

    # Create a JSON message with the current time and a greeting
    message = json.dumps({"time": current_time, "greeting": "Hello, client!"})

    # Send the message to the client
    client_socket.sendall(message.encode())

    # Close the client socket
    client_socket.close()

# Create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, 8080))
server_socket.listen(1)

# Accept a client connection
client_socket, client_address = server_socket.accept()

# Run the task function with the client socket
task_func(client_socket)

# Close the server socket
server_socket.close()