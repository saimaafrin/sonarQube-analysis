import json
import os
import hashlib
import base64
import time
def task_func(file_path, unknown_key):
    with open(file_path, 'r') as f:
        data = json.load(f)
    maindata = data['A'][unknown_key]['maindata'][0]['Info']
    hashed_value = hashlib.sha256(maindata.encode()).hexdigest()
    file_name = f'{time.strftime("%Y%m%d_%H%M%S")}_{hashed_value}.txt'
    with open(file_name, 'w') as f:
        f.write(base64.b64encode(hashed_value.encode()).decode())
    return os.path.abspath(file_name)
file_path = 'data.json'
unknown_key = 'key1'