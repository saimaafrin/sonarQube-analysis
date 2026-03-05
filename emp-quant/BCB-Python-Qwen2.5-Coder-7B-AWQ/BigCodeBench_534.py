import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to an integer
    number = int(num, from_base)
    
    # Sign the number using the private RSA key
    signature = private_key.sign(
        number.to_bytes((number.bit_length() + 7) // 8, byteorder='big'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Combine the number and its signature
    combined = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big') + signature
    
    # Encode the combined data in base64 using the custom alphabet
    base64_encoded = base64.b64encode(combined).decode('utf-8')
    base64_encoded = ''.join([alphabet[base64_encoded.index(char)] for char in base64_encoded])
    
    return base64_encoded