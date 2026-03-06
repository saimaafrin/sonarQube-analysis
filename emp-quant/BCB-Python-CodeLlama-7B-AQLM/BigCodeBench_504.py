import hashlib
import rsa
import base64
def task_func(file_path):
    """
    Generates a signed hash of a file's contents using RSA encryption. The file's contents are hashed using SHA-256,
    and then the hash is signed with a private RSA key stored in 'private.pem'. The signed hash is encoded in base64.

    Parameters:
    file_path (str): The path to the file whose contents are to be signed.

    Returns:
    str: The base64 encoded signed hash of the file.

    Requirements:
    - hashlib
    - rsa
    - base64

    Examples:
    Assuming 'example.txt' contains some text and a valid 'private.pem' is present,
    >>> len(task_func('example.txt')) > 0
    True

    Assuming 'empty.txt' is an empty file and a valid 'private.pem' is present,
    >>> len(task_func('empty.txt')) > 0
    True
    """
    with open(file_path, 'rb') as f:
        data = f.read()

    # Hash the file's contents using SHA-256
    hash_object = hashlib.sha256(data)
    hash_digest = hash_object.hexdigest()

    # Sign the hash using the private key
    with open('private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
        signature = rsa.sign(bytes(hash_digest, 'utf-8'), private_key, 'SHA-256')

    # Encode the signature in base64
    signature_b64 = base64.b64encode(signature)

    return signature_b64