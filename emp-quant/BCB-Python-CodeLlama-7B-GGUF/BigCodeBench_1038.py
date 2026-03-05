
from datetime import datetime
import json

SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    current_time = datetime.now()
    greeting = "Hello, client!"
    message = {"time": current_time, "greeting": greeting}
    message_json = json.dumps(message)
    client_socket.sendall(message_json.encode())
    print(f"Sent message: {message_json}")