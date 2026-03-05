import base64
import json
import zlib
def task_func(data_dict):
    """
    Serializes a dictionary to a JSON string, compresses it using zlib, and then encodes the compressed data with base64.
    The function should output with:
        str: A base64 encoded string that represents the zlib-compressed JSON string of the dictionary.
    """
    # Serialize the dictionary to a JSON string
    json_string = json.dumps(data_dict)

    # Compress the JSON string using zlib
    compressed_json = zlib.compress(json_string.encode())

    # Encode the compressed data with base64
    base64_encoded_string = base64.b64encode(compressed_json)

    return base64_encoded_string.decode()
data_dict = {"key1": "value1", "key2": "value2"}