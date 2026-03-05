import hashlib
import hmac
def task_func(secret, message):
    """
    Generates an HMAC (Hash-based Message Authentication Code) signature for a given message using a secret key.
    The function uses SHA-256 as the hash function to create the HMAC signature.
    """
    # Create an HMAC object using the secret key and SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)

    # Generate the HMAC signature
    hmac_signature = hmac_obj.hexdigest()

    return hmac_signature