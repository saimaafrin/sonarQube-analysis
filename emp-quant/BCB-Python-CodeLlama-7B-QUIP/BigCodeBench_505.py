
import hashlib
import hmac

def task_func(secret, message):
    # Create an HMAC object with the given secret and hash function
    hmac_obj = hmac.HMAC(secret, hashlib.sha256)

    # Update the HMAC object with the given message
    hmac_obj.update(message)

    # Generate the HMAC signature
    signature = hmac_obj.digest()

    # Return the HMAC signature as a hexadecimal string
    return ''.join('{:02x}'.format(ord(c)) for c in signature)