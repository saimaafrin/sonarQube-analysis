
import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to decimal
    num_decimal = int(str(num), from_base)
    
    # Sign the decimal number using the private RSA key
    signature = private_key.sign(
        num_decimal.to_bytes((num_decimal.bit_length() + 7) // 8, byteorder='big'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Encode the signed number in base64 using the custom alphabet
    base64_encoded = base64.b64encode(signature).decode('utf-8')
    encoded_chars = [alphabet.index(char) if char in alphabet else 0 for char in base64_encoded]
    result = ''.join(chr(char) for char in encoded_chars)
    
    return result