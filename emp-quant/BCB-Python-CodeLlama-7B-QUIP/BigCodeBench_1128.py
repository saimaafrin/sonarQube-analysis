
import json
import os
import hashlib
import base64
import time

def task_func(file_path, unknown_key):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract the value to be hashed
    value_to_hash = data['A'][unknown_key]['maindata'][0]['Info']

    # Hash the value
    hash_object = hashlib.sha256(value_to_hash.encode())
    hash_digest = base64.b64encode(hash_object.digest())

    # Write the hash to a new file with a timestamp in the name
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    new_file_name = f"{file_path}-{timestamp}.txt"
    with open(new_file_name, 'w') as f:
        f.write(hash_digest.decode())

    return new_file_name