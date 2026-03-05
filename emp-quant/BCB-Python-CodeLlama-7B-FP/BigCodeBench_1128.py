import json
import os
import hashlib
import base64
import time
def task_func(file_path, unknown_key):
    # Read the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract the value specified by the unknown_key
    value = data['A'][unknown_key]['maindata'][0]['Info']

    # Hash the value using SHA256
    hashed_value = hashlib.sha256(value.encode()).hexdigest()

    # Encode the hashed value in base64
    base64_hash = base64.b64encode(hashed_value.encode()).decode()

    # Create a new file with the timestamp in its name
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
    new_file_path = os.path.join(os.path.dirname(file_path), f'{timestamp}_{base64_hash}.txt')

    # Write the base64-encoded hash to the new file
    with open(new_file_path, 'w') as f:
        f.write(base64_hash)

    # Return the absolute file path of the newly created file
    return new_file_path
file_path = 'example.json'
unknown_key = 'key1'