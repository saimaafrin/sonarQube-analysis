import re
from datetime import time
def task_func(logs: list):
    """
    Analyze the given list of logs for the occurrence of errors and calculate the average time of occurrence of errors.
    The function should output with:
        list: A list of times when errors occurred.
        time: The average time of occurrence of these errors.
    """
    # Initialize variables
    error_times = []
    total_time = 0

    # Iterate through the logs and extract the error times
    for log in logs:
        match = re.search(r"Error at (\d+:\d+:\d+)", log)
        if match:
            error_times.append(time.strptime(match.group(1), "%H:%M:%S"))

    # Calculate the average time of occurrence of errors
    if error_times:
        total_time = sum(error_times, time.timedelta(0))
        average_time = total_time / len(error_times)
    else:
        average_time = None

    # Return the results
    return error_times, average_time