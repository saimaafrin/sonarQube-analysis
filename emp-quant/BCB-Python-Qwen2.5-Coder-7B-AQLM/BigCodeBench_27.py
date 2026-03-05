
import json
import base64
from datetime import datetime

def task_func(data: dict, DATE_FORMAT = "%Y-%m-%d %H:%M:%S") -> str:
    # Add current timestamp to the dictionary
    data['timestamp'] = datetime.now().strftime(DATE_FORMAT)
    
    # Serialize the dictionary to a JSON-formatted string
    json_string = json.dumps(data)
    
    # Encode the JSON string using base64 encoding with ASCII character encoding
    encoded_string = base64.b64encode(json_string.encode('ascii')).decode('ascii')
    
    return encoded_string