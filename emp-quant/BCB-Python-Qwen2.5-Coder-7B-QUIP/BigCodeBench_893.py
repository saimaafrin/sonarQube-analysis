
import re
from datetime import datetime

def task_func(logs: list):
    error_times = []
    total_time = 0

    for log in logs:
        match = re.search(r'\d{2}:\d{2}', log)
        if match:
            error_time = match.group(0)
            error_times.append(error_time)
            total_time += int(error_time)

    average_time = total_time / len(error_times) if error_times else 0

    return {
        'list': error_times,
        'time': average_time
    }