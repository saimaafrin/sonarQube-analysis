
import json
import base64
from datetime import datetime

def task_func(data: dict, DATE_FORMAT = "%Y-%m-%d %H:%M:%S") -> str:
    # Add the current timestamp to the dictionary
    data["timestamp"] = datetime.now().strftime(DATE_FORMAT)

    # Serialize the modified dictionary to a JSON string
    json_str = json.dumps(data)

    # Encode the JSON string using base64 encoding with ASCII character encoding
    base64_str = base64.b64encode(json_str.encode("ascii")).decode("ascii")

    return base64_str