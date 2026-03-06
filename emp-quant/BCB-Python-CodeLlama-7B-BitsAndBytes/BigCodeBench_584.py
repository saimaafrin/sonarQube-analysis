
import rsa
import urllib.request
from hashlib import sha256

def task_func(url):
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Retrieve URL content
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
    except urllib.error.URLError as e:
        raise ValueError("Failed to retrieve URL: {}".format(e))

    # Calculate SHA256 hash of content
    hashed_content = sha256(content).hexdigest()

    # Sign hash with private key
    try:
        signature = private_key.sign(hashed_content, 'SHA-256')
    except rsa.pkcs1.VerificationError as e:
        raise ValueError("Failed to sign hash: {}".format(e))

    # Return public key and signed hash as hexadecimal string
    return public_key, signature.hex(), content