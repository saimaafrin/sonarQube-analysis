
import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to the target base
    num_str = str(num)
    num_str = num_str.zfill(len(num_str))
    num_str = num_str.replace('0', 'a')
    num_str = num_str.replace('1', 'b')
    num_str = num_str.replace('2', 'c')
    num_str = num_str.replace('3', 'd')
    num_str = num_str.replace('4', 'e')
    num_str = num_str.replace('5', 'f')
    num_str = num_str.replace('6', 'g')
    num_str = num_str.replace('7', 'h')
    num_str = num_str.replace('8', 'i')
    num_str = num_str.replace('9', 'j')
    num_str = num_str.replace('a', '0')
    num_str = num_str.replace('b', '1')
    num_str = num_str.replace('c', '2')
    num_str = num_str.replace('d', '3')
    num_str = num_str.replace('e', '4')
    num_str = num_str.replace('f', '5')
    num_str = num_str.replace('g', '6')
    num_str = num_str.replace('h', '7')
    num_str = num_str.replace('i', '8')
    num_str = num_str.replace('j', '9')

    # Sign the converted number with the private key
    signer = padding.PKCS1v15()
    signature = signer.sign(num_str.encode(), private_key)

    # Encode the signed number in base64 using the custom alphabet
    encoded_signature = base64.b64encode(signature)
    encoded_signature = encoded_signature.decode()
    encoded_signature = encoded_signature.replace('+', '*')
    encoded_signature = encoded_signature.replace('/', '&')
    encoded_signature = encoded_signature.replace('=', '^')

    return encoded_signature

signed_num = task_func(num, from_base, to_base, private_key, alphabet)
print(signed_num)