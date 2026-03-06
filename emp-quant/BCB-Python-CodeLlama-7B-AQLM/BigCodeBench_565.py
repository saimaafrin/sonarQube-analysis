import ctypes
import hashlib
import binascii
def task_func(filepath):
    """
    Loads a DLL file from a given filepath, calculates its MD5 and SHA256 hashes,
    and prints these hashes in hexadecimal format. This function is a demonstration
    of file handling, usage of the hashlib library for hash calculations, and binascii
    for hexadecimal conversion. Note that the actual operations performed on the loaded
    DLL are limited to hash calculation.

    Parameters:
    filepath (str): The path of the DLL file.

    Returns:
    str: The actual name of the loaded DLL file.

    Requirements:
    - ctypes
    - hashlib
    - binascii

    Examples:
    >>> with open('libc.so.6', 'w') as f:
    ...     _ = f.write("")
    >>> result = task_func('libc.so.6')
    MD5 Hash: d41d8cd98f00b204e9800998ecf8427e
    SHA256 Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    >>> isinstance(result, str) 
    True
    >>> 'libc.so.6' in result
    True
    """
    # Load the DLL file
    libc = ctypes.CDLL(filepath)
    # Calculate the MD5 hash of the DLL file
    md5 = hashlib.md5()
    md5.update(open(filepath, 'rb').read())
    md5_hash = md5.hexdigest()
    # Calculate the SHA256 hash of the DLL file
    sha256 = hashlib.sha256()
    sha256.update(open(filepath, 'rb').read())
    sha256_hash = sha256.hexdigest()
    # Print the hashes
    print("MD5 Hash: {}".format(md5_hash))
    print("SHA256 Hash: {}".format(sha256_hash))
    # Return the actual name of the loaded DLL file
    return libc.__name__