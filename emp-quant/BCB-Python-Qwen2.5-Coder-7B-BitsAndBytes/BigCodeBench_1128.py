
import json
import os
import hashlib
import base64
import time

def task_func(file_path, unknown_key):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the value from the nested structure
    value_to_hash = data['A'][unknown_key]['maindata'][0]['Info']
    
    # Hash the value using SHA256
    sha256_hash = hashlib.sha256(value_to_hash.encode()).digest()
    
    # Encode the hash in base64
    base64_encoded_hash = base64.b64encode(sha256_hash).decode()
    
    # Create a filename with a timestamp
    timestamp = int(time.time())
    output_file_name = f"hashed_value_{timestamp}.txt"
    output_file_path = os.path.join(os.getcwd(), output_file_name)
    
    # Write the base64-encoded hash to a new file
    with open(output_file_path, 'w') as output_file:
        output_file.write(base64_encoded_hash)
    
    return output_file_path