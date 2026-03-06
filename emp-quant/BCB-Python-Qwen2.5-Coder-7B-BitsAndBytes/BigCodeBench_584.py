
import rsa
import urllib.request
from hashlib import sha256

def task_func(url):
    try:
        # Generate RSA public and private keys
        (public_key, private_key) = rsa.newkeys(512)

        # Retrieve content from the specified URL
        response = urllib.request.urlopen(url)
        url_content = response.read()

        # Calculate SHA256 hash of the URL content
        url_hash = sha256(url_content).digest()

        # Sign the hash with the private key
        signed_hash = rsa.sign(url_hash, private_key, 'SHA-256')

        return public_key, signed_hash.hex(), url_hash

    except ValueError as e:
        print(f"ValueError: {e}")
        raise
    except rsa.pkcs1.VerificationError as e:
        print(f"rsa.pkcs1.VerificationError: {e}")
        raise
    except urllib.error.URLError as e:
        print(f"urllib.error.URLError: {e}")
        raise