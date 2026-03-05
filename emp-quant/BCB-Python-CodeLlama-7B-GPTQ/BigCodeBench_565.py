import ctypes
import hashlib
import binascii
def task_func(filepath):
    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Calculate the MD5 and SHA256 hashes
    md5 = hashlib.md5(dll.read())
    sha256 = hashlib.sha256(dll.read())

    # Convert the hashes to hexadecimal format
    md5_hex = binascii.hexlify(md5.digest()).decode()
    sha256_hex = binascii.hexlify(sha256.digest()).decode()

    # Print the hashes in hexadecimal format
    print(f"MD5: {md5_hex}")
    print(f"SHA256: {sha256_hex}")

    # Return the actual name of the loaded DLL file
    return dll.name
filepath = "path/to/your/dll.dll"