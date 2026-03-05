
import json
import os
import hashlib
import base64
import time

def task_func(file_path, unknown_key):
    # Read the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract the value from the nested structure
    value = data['A'][unknown_key]['maindata'][0]['Info']

    # Hash the value using SHA256
    hashed_value = hashlib.sha256(value.encode()).hexdigest()

    # Base64-encode the hashed value
    base64_encoded_hash = base64.b64encode(hashed_value.encode()).decode()

    # Create a new file with a timestamp in its name
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
    file_name = f'{timestamp}-hashed-value.txt'
    file_path = os.path.join(os.getcwd(), file_name)

    # Write the base64-encoded hash to the new file
    with open(file_path, 'w') as f:
        f.write(base64_encoded_hash)

    # Return the absolute file path of the new file
    return file_path