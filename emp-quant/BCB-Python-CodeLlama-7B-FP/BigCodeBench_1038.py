from datetime import datetime
import json
def task_func(client_socket):
    # Get the current time
    current_time = datetime.now()

    # Create a JSON message
    message = {
        "time": current_time.strftime("%H:%M:%S"),
        "greeting": "Hello, client!"
    }

    # Send the message to the client
    client_socket.sendall(json.dumps(message).encode())

    # Close the socket
    client_socket.close()