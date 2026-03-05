import base64
import hashlib
import hmac
import binascii
def task_func(s, signature, secret_key):
    """
    Validates the HMAC SHA-1 signature of a base64-encoded message against a provided signature using a specified secret key.
    This function first decodes the base64-encoded message, then computes its HMAC SHA-1 hash using the provided secret key, and finally compares this computed hash with the provided signature.
    """
    # Decode the base64-encoded message
    message = base64.b64decode(s)

    # Compute the HMAC SHA-1 hash of the decoded message using the provided secret key
    hmac_sha1 = hmac.new(secret_key.encode(), message, hashlib.sha1)

    # Compare the computed HMAC SHA-1 hash with the provided signature
    if hmac_sha1.hexdigest() == signature:
        return True
    else:
        return False