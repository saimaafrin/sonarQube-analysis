
import ssl
import os
import hashlib

def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    # Secure the client socket using SSL/TLS
    context = ssl.create_default_context()
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)
    client_socket = context.wrap_socket(client_socket, server_side=True)

    # Read the file path requested by the client
    file_path = client_socket.recv(buffer_size).decode()

    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File not found"

    # Calculate the SHA256 hash of the file
    with open(file_path, "rb") as file:
        file_hash = hashlib.sha256(file.read()).hexdigest()

    # Send the hash back to the client
    client_socket.sendall(file_hash.encode())

    # Close the client socket
    client_socket.close()

    return file_hash