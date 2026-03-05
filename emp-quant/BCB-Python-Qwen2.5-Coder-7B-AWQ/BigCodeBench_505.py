import hashlib
import hmac
def task_func(secret, message):
    """
    Generates an HMAC signature for a given message using a secret key.
    
    Args:
    secret (str): The secret key used for generating the HMAC.
    message (str): The message to generate the HMAC for.
    
    Returns:
    str: The HMAC signature of the message, returned as a hexadecimal string.
    """
    # Create a new HMAC object using the secret key and SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    
    # Generate the HMAC signature and return it as a hexadecimal string
    return hmac_obj.hexdigest()