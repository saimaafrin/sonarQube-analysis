
import re
from datetime import time

def task_func(logs: list):
    # Initialize the list of error times and the total time
    error_times = []
    total_time = 0

    # Loop through the logs and find the errors
    for log in logs:
        # Check if the log is an error
        match = re.search(r'Error', log)
        if match:
            # If it is an error, add the time to the list of error times
            error_times.append(time.strptime(log, '%Y-%m-%d %H:%M:%S'))

    # Calculate the average time of occurrence of errors
    if error_times:
        average_time = sum(error_times) / len(error_times)
    else:
        average_time = None

    return error_times, average_time