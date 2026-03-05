
import re
from datetime import datetime

def task_func(logs: list):
    error_times = []
    total_time = 0
    
    for log in logs:
        match = re.search(r'ERROR at (\d{2}:\d{2}:\d{2})', log)
        if match:
            error_time = datetime.strptime(match.group(1), '%H:%M:%S').time()
            error_times.append(error_time)
            total_time += error_time.second + error_time.minute * 60 + error_time.hour * 3600
    
    if error_times:
        average_time = total_time / len(error_times)
        average_time = datetime.fromtimestamp(average_time).strftime('%H:%M:%S')
    else:
        average_time = 'No errors found'
    
    return {'list': error_times, 'time': average_time}