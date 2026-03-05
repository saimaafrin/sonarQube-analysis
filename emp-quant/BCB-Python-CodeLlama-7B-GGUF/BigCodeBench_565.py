
import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Calculate the MD5 and SHA256 hashes
    md5_hash = hashlib.md5(dll.encode()).hexdigest()
    sha256_hash = hashlib.sha256(dll.encode()).hexdigest()

    # Print the hashes in hexadecimal format
    print(f"MD5 hash: {md5_hash}")
    print(f"SHA256 hash: {sha256_hash}")

    # Return the actual name of the loaded DLL file
    return dll.name