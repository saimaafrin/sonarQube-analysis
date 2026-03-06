
import hashlib
import hmac

def task_func(secret, message):
    # Create an HMAC object using the secret key and SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)

    # Generate the HMAC signature
    signature = hmac_obj.hexdigest()

    # Return the signature as a hexadecimal string
    return signature