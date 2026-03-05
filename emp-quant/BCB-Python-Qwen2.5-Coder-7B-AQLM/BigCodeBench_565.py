
import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)
    
    # Calculate MD5 hash
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    md5_hex = binascii.hexlify(md5_hash.digest()).decode('utf-8')
    
    # Calculate SHA256 hash
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    sha256_hex = binascii.hexlify(sha256_hash.digest()).decode('utf-8')
    
    # Return the actual name of the loaded DLL file
    return dll._name