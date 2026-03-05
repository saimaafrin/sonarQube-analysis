
import json
import base64
from datetime import datetime

def task_func(data: dict, DATE_FORMAT = "%Y-%m-%d %H:%M:%S") -> str:
    data["timestamp"] = datetime.now().strftime(DATE_FORMAT)
    json_data = json.dumps(data)
    base64_data = base64.b64encode(json_data.encode("ascii"))
    return base64_data.decode("ascii")