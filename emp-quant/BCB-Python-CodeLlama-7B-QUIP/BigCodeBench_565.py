
import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    with open(filepath, 'rb') as f:
        dll_data = f.read()

    # Calculate the MD5 and SHA256 hashes
    md5_hash = hashlib.md5(dll_data).hexdigest()
    sha256_hash = hashlib.sha256(dll_data).hexdigest()

    # Print the hashes in hexadecimal format
    print(f"MD5: {binascii.b2a_hex(md5_hash)}")
    print(f"SHA256: {binascii.b2a_hex(sha256_hash)}")

    # Return the actual name of the loaded DLL file
    return filepath