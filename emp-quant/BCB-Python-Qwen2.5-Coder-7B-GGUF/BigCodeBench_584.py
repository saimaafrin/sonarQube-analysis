
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
        hash_hex = hash_object.hexdigest()

        # Sign the hash with the private key
        signed_hash = rsa.sign_hash(hash_object, private_key, 'SHA-256')

        return public_key, signed_hash.hex(), hash_object.digest()
    except ValueError as e:
        raise ValueError(f"Error reaching the server or invalid URL: {e}")
    except rsa.pkcs1.VerificationError as e:
        raise rsa.pkcs1.VerificationError(f"Error signing the hash with the RSA private key: {e}")
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"Server not reachable: {e}")