
import base64
import hashlib
import hmac
import binascii

def task_func(s, signature, secret_key):
    # Decode the base64-encoded message
    decoded_message = base64.decodes(s)
    
    # Compute the HMAC SHA-1 hash of the message using the secret key
    hmac_sha1 = hmac.new(secret_key.encode(), decoded_message, hashlib.sha1)
    
    # Get the hexadecimal representation of the computed HMAC SHA-1 hash
    computed_signature = binascii.hexlify(hmac_sha1.digest())
    
    # Compare the computed signature with the provided signature
    return computed_signature == signature.encode()