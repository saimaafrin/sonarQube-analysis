import json
import hashlib
import blake3
def task_func(req_data):
    # Hash the request data with BLAKE3
    blake3_hash = blake3.blake3(req_data.encode())
    # Convert the BLAKE3 hash to a hexadecimal representation
    blake3_hex = blake3_hash.hexdigest()
    # Generate an MD5 hash of the BLAKE3 hash for demonstration purposes
    md5_hash = hashlib.md5(blake3_hex.encode()).hexdigest()
    return (blake3_hex, md5_hash)
req_data = json.dumps({"key1": "value1", "key2": "value2"})