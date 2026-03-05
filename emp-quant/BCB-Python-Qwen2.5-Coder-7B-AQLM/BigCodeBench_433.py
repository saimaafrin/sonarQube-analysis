
import base64
import hashlib
import hmac
import binascii

def task_func(s, signature, secret_key):
    # Decode the base64-encoded message
    decoded_message = base64.b64decode(s)
    
    # Compute the HMAC SHA-1 hash of the decoded message using the secret key
    hmac_signature = hmac.new(secret_key.encode(), decoded_message, hashlib.sha1).digest()
    
    # Convert the computed HMAC signature to a hexadecimal string
    computed_signature = binascii.hexlify(hmac_signature).decode()
    
    # Compare the computed signature with the provided signature
    return computed_signature == signature