import json
import os
import hashlib
import base64
import time
def task_func(file_path, unknown_key):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the value to be hashed
    value_to_hash = data['A'][unknown_key]['maindata'][0]['Info']
    
    # Hash the value using SHA256
    sha256_hash = hashlib.sha256(value_to_hash.encode()).digest()
    
    # Encode the hash in base64
    base64_hash = base64.b64encode(sha256_hash).decode()
    
    # Create a timestamp
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    # Define the output file path
    output_file_path = os.path.join(os.getcwd(), f"{timestamp}.txt")
    
    # Write the base64-encoded hash to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(base64_hash)
    
    # Return the absolute file path of the newly created file
    return os.path.abspath(output_file_path)