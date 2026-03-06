
import json
import hashlib
import blake3

def task_func(req_data):
    # Convert the request data to bytes if it's not already
    if isinstance(req_data, dict):
        req_data = json.dumps(req_data)
    
    # Hash the request data using BLAKE3
    b3_hash = blake3.blake3(req_data.encode('utf-8')).hexdigest()
    
    # Generate an MD5 hash of the BLAKE3 hash for demonstration purposes
    md5_hash = hashlib.md5(b3_hash.encode('utf-8')).hexdigest()
    
    return b3_hash, md5_hash