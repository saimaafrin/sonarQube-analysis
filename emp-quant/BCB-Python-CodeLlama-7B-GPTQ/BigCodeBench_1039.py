import ssl
import os
import hashlib
def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    # Secure the client socket using SSL/TLS
    context = ssl.create_default_context()
    context.load_certificate(certfile=cert_file)
    context.load_privatekey(keyfile=key_file)
    client_socket = context.wrap_socket(client_socket, server_side=True)

    # Read the file path requested by the client
    file_path = client_socket.recv(buffer_size).decode()

    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File not found"

    # Calculate the SHA256 hash of the file
    with open(file_path, "rb") as file:
        file_hash = hashlib.sha256()
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            file_hash.update(data)

    # Return the SHA256 hash of the file
    return file_hash.hexdigest()