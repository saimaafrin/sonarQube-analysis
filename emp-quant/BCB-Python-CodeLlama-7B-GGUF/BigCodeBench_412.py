
import json
import base64
import unicodedata

def task_func(json_file: str) -> dict:
    with open(json_file, 'r') as f:
        data = json.load(f)

    normalized_data = {}
    for key, value in data.items():
        decoded_value = base64.b64decode(value).decode('utf-8')
        normalized_value = unicodedata.normalize('NFC', decoded_value)
        normalized_data[key] = normalized_value

    return normalized_data