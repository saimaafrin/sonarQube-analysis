import rsa
from cryptography.fernet import Fernet
from base64 import b64encode
def task_func(file_path):
    """
    Generates RSA public and private keys and uses Fernet symmetric encryption to encrypt the contents
    of a specified file. The Fernet key is then encrypted with the public RSA key. The encrypted file
    contents and the encrypted Fernet key are saved in separate files.

    This method demonstrates a hybrid encryption approach where symmetric encryption is used for the file
    contents and asymmetric encryption for the encryption key.

    Parameters:
    file_path (str): The path to the file to be encrypted.

    Returns:
    PublicKey: The RSA public key.
    str: The filename of the encrypted file.
    str: The filename of the file containing the encrypted Fernet key.

    Requirements:
    - rsa
    - cryptography.fernet.Fernet
    - base64.b64encode

    Examples:
    >>> pub_key, encrypted_file, encrypted_key_file = task_func('my_file.txt')
    >>> len(pub_key.save_pkcs1()) > 100
    True
    >>> encrypted_file.endswith('.encrypted')
    True
    >>> encrypted_key_file.endswith('.encrypted')
    True
    """
    # Generate RSA keys
    priv_key = rsa.PrivateKey.generate(2048)
    pub_key = priv_key.publickey()

    # Encrypt file contents with Fernet
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    fernet = Fernet(Fernet.generate_key())
    encrypted_file_contents = fernet.encrypt(file_contents)

    # Encrypt Fernet key with RSA
    encrypted_fernet_key = pub_key.encrypt(
        b64encode(fernet.encrypt(Fernet.generate_key())),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save RSA keys
    priv_key_file = 'private_key.pem'
    pub_key_file = 'public_key.pem'
    with open(priv_key_file, 'wb') as f:
        f.write(priv_key.save_pkcs1())
    with open(pub_key_file, 'wb') as f:
        f.write(pub_key.save_pkcs1())

    # Save encrypted file contents and encrypted Fernet key
    encrypted_file = file_path + '.encrypted'
    encrypted_key_file = file_path + '.encrypted.key'
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_file_contents)
    with open(encrypted_key_file, 'wb') as f:
        f.write(encrypted_fernet_key)

    return pub_key, encrypted_file, encrypted_key_file