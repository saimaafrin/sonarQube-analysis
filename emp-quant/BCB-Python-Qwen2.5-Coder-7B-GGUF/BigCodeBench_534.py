
import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to the target base
    converted_num = int(num, from_base)
    converted_num_str = format(converted_num, f'0{to_base}b')
    
    # Sign the converted number using the private RSA key
    signature = private_key.sign(
        converted_num_str.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Encode the signed number in base64 using the custom alphabet
    base64_encoded = base64.b64encode(signature).decode()
    base64_encoded = ''.join([alphabet[base64_encoded[i]] for i in range(len(base64_encoded))])
    
    return base64_encoded