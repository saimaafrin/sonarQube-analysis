
import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)
    
    # Calculate MD5 hash
    with open(filepath, 'rb') as f:
        md5_hash = hashlib.md5(f.read()).hexdigest()
    
    # Calculate SHA256 hash
    with open(filepath, 'rb') as f:
        sha256_hash = hashlib.sha256(f.read()).hexdigest()
    
    # Print the hashes
    print(f"MD5: {md5_hash}")
    print(f"SHA256: {sha256_hash}")
    
    # Return the actual name of the loaded DLL file
    return dll._name