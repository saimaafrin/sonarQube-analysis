
import json
import hashlib
import blake3

def task_func(req_data):
    # Hash the request data with BLAKE3
    blake3_hash = blake3.blake3(req_data.encode('utf-8')).hexdigest()

    # Generate an MD5 hash of the BLAKE3 hash for demonstration
    md5_hash = hashlib.md5(blake3_hash.encode('utf-8')).hexdigest()

    # Return a tuple containing the BLAKE3 and MD5 hashes
    return (blake3_hash, md5_hash)