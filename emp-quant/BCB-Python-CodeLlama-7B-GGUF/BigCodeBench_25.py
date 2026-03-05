
import base64
import json
import zlib

def task_func(data_dict):
    # Serialize the dictionary to a JSON string
    json_string = json.dumps(data_dict)

    # Compress the JSON string using zlib
    compressed_data = zlib.compress(json_string.encode())

    # Encode the compressed data with base64
    base64_encoded_data = base64.b64encode(compressed_data)

    # Return the base64 encoded string
    return base64_encoded_data.decode()