import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to a decimal integer
    decimal_num = int(num, from_base)
    
    # Sign the decimal number using the private RSA key
    signature = private_key.sign(
        decimal_num.to_bytes((decimal_num.bit_length() + 7) // 8, byteorder='big'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Encode the signed number in base64 using the custom alphabet
    base64_encoded = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
    base64_encoded = ''.join([alphabet[base64_encoded[i]] for i in range(len(base64_encoded))])
    
    return base64_encoded