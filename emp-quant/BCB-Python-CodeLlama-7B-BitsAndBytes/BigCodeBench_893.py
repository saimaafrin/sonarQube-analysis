
import re
from datetime import time

def task_func(logs: list):
    # Initialize variables to store the times and the number of errors
    times = []
    num_errors = 0

    # Iterate through the logs and extract the time and error message
    for log in logs:
        match = re.search(r'(\d{2}:\d{2}:\d{2}) - ERROR - (.+)', log)
        if match:
            time = time.fromisoformat(match.group(1))
            error_message = match.group(2)
            times.append(time)
            num_errors += 1

    # Calculate the average time of occurrence of errors
    average_time = sum(times) / num_errors

    # Return the list of times and the average time
    return times, average_time

times, average_time = task_func(logs)
print(times)
print(average_time)