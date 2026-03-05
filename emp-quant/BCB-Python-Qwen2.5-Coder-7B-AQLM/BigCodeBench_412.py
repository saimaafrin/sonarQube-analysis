
import json
import base64
import unicodedata

def task_func(json_file: str) -> dict:
    result = {}
    with open(json_file, 'r') as file:
        data = json.load(file)
        for key, value in data.items():
            decoded_bytes = base64.b64decode(value)
            decoded_string = decoded_bytes.decode('utf-8')
            normalized_string = unicodedata.normalize('NFC', decoded_string)
            result[key] = normalized_string
    return result