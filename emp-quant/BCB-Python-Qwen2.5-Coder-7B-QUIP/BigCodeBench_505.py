
import hashlib
import hmac

def task_func(secret, message):
    # Create a new HMAC object using the secret key and SHA-256 as the hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    # Return the hexadecimal representation of the HMAC signature
    return hmac_obj.hexdigest()