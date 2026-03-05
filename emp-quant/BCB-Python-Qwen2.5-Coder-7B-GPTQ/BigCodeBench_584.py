import rsa
import urllib.request
from hashlib import sha256
def task_func(url):
    try:
        # Generate RSA public and private keys
        public_key, private_key = rsa.newkeys(512)

        # Retrieve content from the specified URL
        response = urllib.request.urlopen(url)
        content = response.read()

        # Calculate SHA256 hash of the URL content
        hash_object = sha256(content)
        hashed_content = hash_object.digest()

        # Sign the hash with the private key
        signed_hash = rsa.sign(hashed_content, private_key, 'SHA-256')

        # Return the public key and the signed hash as a hexadecimal string
        return public_key, signed_hash.hex(), hashed_content

    except ValueError as e:
        raise ValueError(f"Error reaching the server: {e}")
    except rsa.pkcs1.VerificationError as e:
        raise rsa.pkcs1.VerificationError(f"Error signing the hash: {e}")
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"Server not reachable: {e}")
url = "https://www.example.com"