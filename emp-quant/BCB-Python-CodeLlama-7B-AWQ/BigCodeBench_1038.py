from datetime import datetime
import json
def task_func(client_socket):
    # Get the current time
    current_time = datetime.now()

    # Create a JSON message with the current time and a greeting
    message = {
        "time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "greeting": "Hello, client!"
    }

    # Convert the message to JSON format
    message_json = json.dumps(message)

    # Send the JSON message to the client
    client_socket.sendall(message_json.encode())

    # Close the client socket
    client_socket.close()