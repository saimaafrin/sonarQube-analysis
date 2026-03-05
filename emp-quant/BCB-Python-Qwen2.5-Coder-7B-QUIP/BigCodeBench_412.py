
import json
import base64
import unicodedata

def task_func(json_file: str) -> dict:
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    normalized_dict = {}
    for key, value in data.items():
        decoded_value = base64.decodebytes(value.encode('utf-8'))
        normalized_value = unicodedata.normalize('NFC', decoded_value.decode('utf-8'))
        normalized_dict[key] = normalized_value
    
    return normalized_dict