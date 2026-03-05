
import socket
import select
import queue
from datetime import datetime, timedelta

def task_func(
    server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5
):
    start_time = datetime.now()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)
    print(f"Server started on {server_address}:{server_port}")

    inputs = [server_socket]
    outputs = []
    message_queues = {}

    try:
        while datetime.now() - start_time < timedelta(seconds=run_duration):
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is server_socket:
                    connection, client_address = s.accept()
                    connection.setblocking(False)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                    print(f"New connection from {client_address}")
                else:
                    data = s.recv(buffer_size)
                    if data:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        message_queues[s].put(f"{data.decode()} - {current_time}")
                        if s not in outputs:
                            outputs.append(s)
                    else:
                        print(f"Closing connection to {s.getpeername()}")
                        inputs.remove(s)
                        outputs.remove(s)
                        s.close()
                        del message_queues[s]

            for s in writable:
                try:
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    outputs.remove(s)
                else:
                    print(f"Sending message to {s.getpeername()}: {next_msg}")
                    s.send(next_msg.encode())

            for s in exceptional:
                print(f"Handling exceptional condition for {s.getpeername()}")
                inputs.remove(s)
                outputs.remove(s)
                s.close()
                del message_queues[s]

    finally:
        server_socket.close()
        print("Server stopped")

    return f"Server ran for {run_duration} seconds"