import ctypes
import hashlib
import binascii
def task_func(filepath):
    """
    Loads a DLL file from a given filepath, calculates its MD5 and SHA256 hashes, and prints these hashes in hexadecimal format.
    This function is a demonstration of file handling, usage of the hashlib library for hash calculations, and binascii for hexadecimal conversion.
    Note that the actual operations performed on the loaded DLL are limited to hash calculation.
    """
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Calculate the MD5 and SHA256 hashes
    md5_hash = hashlib.md5(dll.read()).hexdigest()
    sha256_hash = hashlib.sha256(dll.read()).hexdigest()

    # Print the hashes in hexadecimal format
    print(f"MD5 hash: {md5_hash}")
    print(f"SHA256 hash: {sha256_hash}")

    # Return the actual name of the loaded DLL file
    return os.path.basename(filepath)
filepath = "path/to/your/dll.dll"