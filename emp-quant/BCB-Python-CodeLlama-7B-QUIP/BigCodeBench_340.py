
import json
import hashlib
import blake3

def task_func(req_data):
    # Hash the request data with BLAKE3
    blake3_hash = blake3.blake3_hash(req_data)
    # Convert the BLAKE3 hash to a hexadecimal representation
    hex_blake3_hash = blake3_hash.hexdigest()
    # Generate an MD5 hash of the hexadecimal BLAKE3 representation
    md5_hash = hashlib.md5(hex_blake3_hash.encode()).hexdigest()
    return (hex_blake3_hash, md5_hash)