
import base64
import hashlib
import hmac
import binascii

def task_func(s, signature, secret_key):
    # Decode the base64-encoded message
    message = base64.b64decode(s)

    # Compute the HMAC SHA-1 hash of the message using the secret key
    hmac_hash = hmac.new(secret_key.encode(), message, hashlib.sha1)

    # Compare the computed hash with the provided signature
    return hmac_hash.hexdigest() == signature