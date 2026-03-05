
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    public_key, private_key = rsa.newkeys(2048)

    # Generate a random password for AES encryption
    password = get_random_bytes(16)

    # Generate a random nonce for AES encryption
    nonce = get_random_bytes(16)

    # Encrypt the private key using AES
    cipher = AES.new(password, AES.MODE_CFB, nonce)
    encrypted_private_key = cipher.encrypt(private_key)

    # Encode the encrypted private key to base64 for storage
    encrypted_private_key_base64 = b64encode(encrypted_private_key)

    # Generate a filename based on the hex representation of 8 random bytes
    filename = f"private_key_{os.urandom(8).hex()}.txt"

    # Save the encrypted private key to a file
    with open(filename, "w") as file:
        file.write(encrypted_private_key_base64.decode())

    # Return the public key, filename, password, and nonce
    return {
        "rsa.PublicKey": public_key,
        "filename": filename,
        "password": password,
        "nonce": nonce
    }