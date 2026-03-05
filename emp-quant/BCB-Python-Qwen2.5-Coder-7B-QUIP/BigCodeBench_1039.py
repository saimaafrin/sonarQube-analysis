
import ssl
import os
import hashlib
def task_func(client_socket, cert_file, key_file, buffer_size=1024):
    try:
        # Wrap the client socket with SSL/TLS
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_cert_chain(cert_file, key_file)
        client_socket = context.wrap_socket(client_socket, server_hostname='example.com')

        # Receive the file path from the client
        file_path = client_socket.recv(buffer_size).decode('utf-8')

        # Check if the file exists
        if not os.path.exists(file_path):
            return 'File not found'

        # Calculate the SHA256 hash of the file
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                sha256_hash.update(data)

        # Send the SHA256 hash back to the client
        client_socket.sendall(sha256_hash.hexdigest().encode('utf-8'))

    except Exception as e:
        return str(e)

    return sha256_hash.hexdigest()