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
        while datetime.now() - start_time < timedelta(seconds=run_duration):
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is server_socket:
                    connection, client_address = s.accept()
                    connection.setblocking(False)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                else:
                    data = s.recv(buffer_size)
                    if data:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        response = data.decode() + " " + current_time
                        message_queues[s].put(response)
                        if s not in outputs:
                            outputs.append(s)
                    else:
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
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                s.close()
                del message_queues[s]

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        server_socket.close()
        for s in inputs:
            s.close()

    return "Server stopped after run duration"