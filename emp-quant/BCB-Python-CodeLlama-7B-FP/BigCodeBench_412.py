import json
import base64
import unicodedata
def task_func(json_file: str) -> dict:
    """
    Reads a JSON file where each key is a unique identifier, and the corresponding value is a base64 encoded string.
    After decoding, it applies Unicode normalization form C (NFC) to each decoded string to ensure the canonical composition of characters.
    The function returns a dictionary where the keys are preserved, and the values are the normalized, decoded strings.
    Decoding is performed using the UTF-8 encoding scheme.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)

    normalized_data = {}
    for key, value in data.items():
        decoded_value = base64.b64decode(value).decode('utf-8')
        normalized_value = unicodedata.normalize('NFC', decoded_value)
        normalized_data[key] = normalized_value

    return normalized_data