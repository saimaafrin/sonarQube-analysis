
import re
from datetime import time

def task_func(logs: list):
    # Initialize variables
    error_times = []
    total_time = 0

    # Iterate over logs
    for log in logs:
        # Check if log contains error
        if re.search(r"error", log, re.IGNORECASE):
            # Extract time from log
            time_str = re.search(r"\d{2}:\d{2}:\d{2}", log).group()
            time_obj = time.fromisoformat(time_str)

            # Add time to list
            error_times.append(time_obj)

    # Calculate average time of occurrence of errors
    if len(error_times) > 0:
        average_time = sum(error_times) / len(error_times)
    else:
        average_time = None

    # Return list and average time
    return error_times, average_time