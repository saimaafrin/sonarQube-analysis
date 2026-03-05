
import json
from datetime import datetime

def task_func(json_data):
    data = json.loads(json_data)
    utc_datetime_str = data['utc_datetime']
    utc_datetime = datetime.strptime(utc_datetime_str, '%Y-%m-%dT%H:%M:%SZ')
    return utc_datetime.weekday() >= 5  # 5 and 6 correspond to Saturday and Sunday