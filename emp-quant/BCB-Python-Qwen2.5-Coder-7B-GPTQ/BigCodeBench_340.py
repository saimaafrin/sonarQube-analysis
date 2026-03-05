import json
import hashlib
import blake3
def task_func(req_data):
    # Convert the request data to a JSON string
    json_data = json.dumps(req_data)
    
    # Create a BLAKE3 hash object
    blake3_hash = blake3.blake3()
    
    # Update the hash object with the JSON data
    blake3_hash.update(json_data.encode('utf-8'))
    
    # Get the hexadecimal representation of the BLAKE3 hash
    blake3_hex = blake3_hash.hexdigest()
    
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the MD5 hash object with the BLAKE3 hexadecimal representation
    md5_hash.update(blake3_hex.encode('utf-8'))
    
    # Get the hexadecimal representation of the MD5 hash
    md5_hex = md5_hash.hexdigest()
    
    # Return a tuple with the BLAKE3 and MD5 hexadecimal representations
    return blake3_hex, md5_hex