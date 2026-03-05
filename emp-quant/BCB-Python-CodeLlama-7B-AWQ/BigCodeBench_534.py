import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to the target base
    converted_num = str(np.base_repr(num, from_base))

    # Sign the converted number with the private RSA key
    signer = padding.PKCS1v15()
    signature = signer.sign(converted_num.encode(), private_key)

    # Encode the signed number in base64 using the custom alphabet
    encoded_signature = base64.b64encode(signature).decode()

    # Return the base64-encoded signed number
    return encoded_signature
num = 1234567890
from_base = 10
to_base = 2