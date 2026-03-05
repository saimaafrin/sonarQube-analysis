
import json
from datetime import datetime

def task_func(json_data):
    utc_datetime = json_data['utc_datetime']
    return utc_datetime.weekday() == 6 or utc_datetime.weekday() == 7