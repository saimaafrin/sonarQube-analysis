import base64
import json
import zlib
def task_func(data_dict):
    """
    Serializes a dictionary to a JSON string, compresses it using zlib, and then encodes the compressed data with base64.
    The function should output with:
        str: A base64 encoded string that represents the zlib-compressed JSON string of the dictionary.
    """
    json_str = json.dumps(data_dict)
    compressed_data = zlib.compress(json_str.encode())
    base64_encoded_data = base64.b64encode(compressed_data)
    return base64_encoded_data.decode()
data_dict = {"key1": "value1", "key2": "value2"}