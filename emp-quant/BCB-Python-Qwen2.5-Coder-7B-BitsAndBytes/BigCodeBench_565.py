
import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL using ctypes
    dll = ctypes.CDLL(filepath)
    
    # Initialize hash objects
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    # Open the file in binary mode
    with open(filepath, 'rb') as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
            sha256_hash.update(byte_block)
    
    # Get the hexadecimal digest of the hashes
    md5_hex = binascii.hexlify(md5_hash.digest()).decode('utf-8')
    sha256_hex = binascii.hexlify(sha256_hash.digest()).decode('utf-8')
    
    # Print the results
    print(f"MD5: {md5_hex}")
    print(f"SHA256: {sha256_hex}")
    
    # Return the filename
    return dll._name.split('\\')[-1]