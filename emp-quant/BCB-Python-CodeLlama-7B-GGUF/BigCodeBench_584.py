
import rsa
import urllib.request
from hashlib import sha256

def task_func(url):
    # Generate RSA keys
    private_key = rsa.key.generate(2048)
    public_key = private_key.publickey()

    # Retrieve URL content
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
    except (urllib.error.URLError, ValueError):
        raise

    # Calculate SHA256 hash of content
    hashed_content = sha256(content).hexdigest()

    # Sign hash with private key
    try:
        signature = private_key.sign(hashed_content, 'SHA-256')
    except rsa.pkcs1.VerificationError:
        raise

    # Return public key and signed hash
    return public_key, signature.hex(), content