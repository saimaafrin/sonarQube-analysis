
import base64
import hashlib
import hmac
import binascii

def task_func(s, signature, secret_key):
    # Decode the base64-encoded message
    decoded_message = base64.b64decode(s)
    
    # Create a new HMAC object using the secret key and SHA-1 as the hash function
    hmac_obj = hmac.new(secret_key.encode(), decoded_message, hashlib.sha1)
    
    # Get the hexadecimal representation of the HMAC digest
    computed_signature = hmac_obj.hexdigest()
    
    # Compare the computed signature with the provided signature
    return computed_signature == signature