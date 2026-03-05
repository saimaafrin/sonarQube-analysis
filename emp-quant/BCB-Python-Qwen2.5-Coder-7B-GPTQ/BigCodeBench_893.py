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
            total_time += error_time.hour * 3600 + error_time.minute * 60 + error_time.second
    
    if error_times:
        average_time_seconds = total_time / len(error_times)
        average_time = datetime(1900, 1, 1) + timedelta(seconds=average_time_seconds)
        average_time = average_time.time()
    else:
        average_time = None
    
    return error_times, average_time