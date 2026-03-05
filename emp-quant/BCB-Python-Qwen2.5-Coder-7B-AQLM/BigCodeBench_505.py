
import hashlib
import hmac

def task_func(secret, message):
    # Create a new HMAC object using the secret key and SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    # Generate the HMAC signature and return it as a hexadecimal string
    return hmac_obj.hexdigest()