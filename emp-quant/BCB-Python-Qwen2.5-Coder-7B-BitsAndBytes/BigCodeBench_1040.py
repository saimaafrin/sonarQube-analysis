
import socket
import select
import queue
from datetime import datetime, timedelta

def task_func(
    server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5
):
    start_time = datetime.now()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)
    server_socket.setblocking(False)

    inputs = [server_socket]
    outputs = []
    message_queues = {}

    try:
        while (datetime.now() - start_time) < timedelta(seconds=run_duration):
            readable, writable, exceptional = select.select(inputs, outputs, inputs, 1)

            for s in readable:
                if s is server_socket:
                    connection, client_address = s.accept()
                    print(f"Connection from {client_address}")
                    connection.setblocking(False)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                else:
                    data = s.recv(buffer_size)
                    if data:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        response_data = f"{data.decode()} {current_time}"
                        message_queues[s].put(response_data)
                        if s not in outputs:
                            outputs.append(s)
                    else:
                        print(f"Closing connection to {s.getpeername()}")
                        if s in outputs:
                            outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        del message_queues[s]

            for s in writable:
                try:
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    outputs.remove(s)
                else:
                    s.send(next_msg.encode())

            for s in exceptional:
                print(f"Handling exception for {s.getpeername()}")
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    finally:
        server_socket.close()

    return "Server stopped after running for 5 seconds."