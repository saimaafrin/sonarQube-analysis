import json
import os
import hashlib
import base64
import time
def task_func(file_path, unknown_key):
    with open(file_path, 'r') as f:
        data = json.load(f)
    value = data['A'][unknown_key]['maindata'][0]['Info']
    hashed_value = hashlib.sha256(value.encode()).digest()
    hashed_value_base64 = base64.b64encode(hashed_value).decode()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_file_name = f"{timestamp}-{hashed_value_base64}.txt"
    output_file_path = os.path.join(os.getcwd(), output_file_name)
    with open(output_file_path, 'w') as f:
        f.write(hashed_value_base64)
    return output_file_path
file_path = "example.json"
unknown_key = "key1"