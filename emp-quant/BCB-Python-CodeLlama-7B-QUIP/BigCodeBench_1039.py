
import ssl
import os
import hashlib

def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    # Secure the client socket using SSL/TLS
    context = ssl.create_default_context()
    ssl_client = context.wrap_client_socket(client_socket)

    # Read the file requested by the client
    file_path = ssl_client.recv(buffer_size)
    if not os.path.exists(file_path):
        return "File not found"
    with open(file_path, "rb") as f:
        file_content = f.read()

    # Calculate the SHA256 hash of the file
    hash = hashlib.sha256(file_content).hexdigest()

    # Send the hash back to the client
    ssl_client.send(hash)

    # Close the client socket
    ssl_client.close()

    return hash