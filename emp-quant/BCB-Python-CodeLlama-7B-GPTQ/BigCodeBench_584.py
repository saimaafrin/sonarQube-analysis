import rsa
import urllib.request
from hashlib import sha256
def task_func(url):
    # Generate RSA keys
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.backends.openssl.backend
    )
    public_key = key.public_key()

    # Retrieve URL content
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
    except urllib.error.URLError as e:
        raise ValueError(f"Error retrieving URL: {e}")

    # Calculate SHA256 hash
    hashed_content = sha256(content).hexdigest()

    # Sign hash with private key
    try:
        signature = key.sign(hashed_content, padding.PKCS1v15(), hashes.SHA256())
    except rsa.pkcs1.VerificationError as e:
        raise ValueError(f"Error signing hash: {e}")

    # Return public key and signed hash
    return public_key, signature.hex(), hashed_content
url = "https://www.example.com"