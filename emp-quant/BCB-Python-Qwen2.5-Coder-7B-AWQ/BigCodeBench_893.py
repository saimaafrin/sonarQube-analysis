import re
from datetime import datetime
def task_func(logs: list):
    error_times = []
    for log in logs:
        match = re.search(r'\[(.*?)\]', log)
        if match:
            time_str = match.group(1)
            error_times.append(datetime.strptime(time_str, '%H:%M:%S'))
    
    if not error_times:
        return {'list': [], 'time': None}
    
    total_seconds = sum((time_obj - error_times[0]).total_seconds() for time_obj in error_times)
    average_time = (error_times[0] + timedelta(seconds=total_seconds / len(error_times))).strftime('%H:%M:%S')
    
    return {'list': [time_obj.strftime('%H:%M:%S') for time_obj in error_times], 'time': average_time}