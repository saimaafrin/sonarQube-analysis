
import re
from datetime import datetime

def task_func(logs: list):
    error_times = []
    
    # Regular expression to find timestamps in the log entries
    timestamp_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'
    
    for log in logs:
        match = re.search(timestamp_pattern, log)
        if match:
            # Extract the timestamp part from the log entry
            timestamp_str = match.group(1)
            # Convert the timestamp string to a datetime object
            error_time = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
            # Append the datetime object to the list
            error_times.append(error_time)
    
    # Calculate the average time of occurrence of errors
    if error_times:
        total_seconds = sum((error_time - error_times[0]).total_seconds() for error_time in error_times)
        average_time = (error_times[0] + timedelta(seconds=total_seconds / len(error_times))).strftime('%H:%M:%S')
    else:
        average_time = 'No errors found'
    
    return {'list': [error_time.strftime('%H:%M:%S') for error_time in error_times], 'time': average_time}