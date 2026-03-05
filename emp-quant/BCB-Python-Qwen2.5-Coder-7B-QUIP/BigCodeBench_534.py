
import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to the target base
    converted_num = int(num, from_base)
    converted_num = converted_num.to_bytes((converted_num.bit_length() // 8) + 1, 'big').lstrip(b'\x00')

    # Sign the converted number using the private key
    signer = private_key.signer(hashes.SHA256())
    signer.update(converted_num)
    signature = signer.signature

    # Encode the signed number in base64 using the custom alphabet
    base64_signature = base64.b64encode(signature, alphabet).decode('utf-8')

    return base64_signature