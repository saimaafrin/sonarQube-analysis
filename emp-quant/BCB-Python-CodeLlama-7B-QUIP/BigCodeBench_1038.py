
from datetime import datetime
import json

SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    greeting = "Hello, {}! The current time is {}".format(client_socket.getpeername()[0], current_time)
    json_greeting = json.dumps(greeting)
    client_socket.send(json_greeting)
    client_socket.close()