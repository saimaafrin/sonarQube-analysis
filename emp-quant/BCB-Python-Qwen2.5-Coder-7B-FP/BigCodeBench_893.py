import re
from datetime import datetime
def task_func(logs: list):
    error_times = []
    total_time = 0
    count = 0

    for log in logs:
        match = re.search(r'\[(\d{2}:\d{2}:\d{2})\] ERROR', log)
        if match:
            error_time_str = match.group(1)
            error_time = datetime.strptime(error_time_str, '%H:%M:%S').time()
            error_times.append(error_time)
            total_time += error_time.hour * 3600 + error_time.minute * 60 + error_time.second
            count += 1

    if count == 0:
        average_time = None
    else:
        average_time = datetime.fromtimestamp(total_time // count).time()

    return error_times, average_time