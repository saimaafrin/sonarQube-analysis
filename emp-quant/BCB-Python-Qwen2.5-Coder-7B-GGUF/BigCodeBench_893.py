
import re
from datetime import datetime

def task_func(logs: list):
    error_times = []
    total_time = 0
    error_count = 0

    for log in logs:
        # Use regular expression to find the time in the log entry
        match = re.search(r'\d{2}:\d{2}:\d{2}', log)
        if match:
            error_time_str = match.group()
            error_time = datetime.strptime(error_time_str, '%H:%M:%S').time()
            error_times.append(error_time)
            total_time += error_time.hour * 3600 + error_time.minute * 60 + error_time.second
            error_count += 1

    if error_count > 0:
        average_time_seconds = total_time // error_count
        average_time = datetime.strptime(str(average_time_seconds), '%S').time()
    else:
        average_time = None

    return error_times, average_time