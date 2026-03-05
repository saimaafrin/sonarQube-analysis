
import json
import hashlib
import blake3

def task_func(req_data):
    # Convert the request data to a JSON string
    req_data_json = json.dumps(req_data)
    
    # Hash the JSON string using BLAKE3
    blake3_hash = blake3.blake3(req_data_json.encode()).hexdigest()
    
    # Convert the BLAKE3 hash to hexadecimal
    blake3_hex = blake3_hash
    
    # Generate an MD5 hash of the BLAKE3 hash
    md5_hash = hashlib.md5(blake3_hash.encode()).hexdigest()
    
    # Return the results as a tuple
    return blake3_hex, md5_hash