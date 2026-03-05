
import json
import hashlib
import blake3

def task_func(req_data):
    # Convert the request data to a JSON string
    json_data = json.dumps(req_data)
    
    # Hash the JSON string using BLAKE3
    blake3_hash = blake3.blake3(json_data.encode()).hexdigest()
    
    # Generate an MD5 hash of the BLAKE3 hash for demonstration purposes
    md5_hash = hashlib.md5(blake3_hash.encode()).hexdigest()
    
    # Return the results as a tuple
    return blake3_hash, md5_hash