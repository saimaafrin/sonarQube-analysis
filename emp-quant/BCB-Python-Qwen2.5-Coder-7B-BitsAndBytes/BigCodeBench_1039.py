
import ssl
import os
import hashlib

def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    try:
        # Wrap the client socket with SSL context
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        secure_client_socket = context.wrap_socket(client_socket, server_side=True)

        # Receive the file path from the client
        file_path = secure_client_socket.recv(buffer_size).decode('utf-8').strip()

        # Check if the file exists
        if not os.path.exists(file_path):
            return 'File not found'

        # Calculate the SHA256 hash of the file
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while chunk := file.read(buffer_size):
                sha256_hash.update(chunk)

        # Send the SHA256 hash back to the client
        secure_client_socket.sendall(sha256_hash.hexdigest().encode('utf-8'))

        # Close the secure client socket
        secure_client_socket.close()

        return sha256_hash.hexdigest()

    except Exception as e:
        return f'Error: {str(e)}'