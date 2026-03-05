import re
from datetime import time
def task_func(logs: list):
    """
    Analyze the given list of logs for the occurrence of errors and calculate the average time of occurrence of errors.
    :param logs: A list of logs
    :return: A list of times when errors occurred and the average time of occurrence of these errors
    """
    # Initialize variables
    error_times = []
    total_time = 0
    count = 0

    # Iterate through the logs
    for log in logs:
        # Check if the log contains an error
        if re.search(r'error', log, re.IGNORECASE):
            # Extract the time from the log
            time_str = re.search(r'\d{2}:\d{2}:\d{2}', log).group()
            time_obj = time.strptime(time_str, '%H:%M:%S')

            # Add the time to the list of error times
            error_times.append(time_obj)

            # Increment the total time and count
            total_time += time_obj.second
            count += 1

    # Calculate the average time of occurrence of errors
    average_time = total_time / count

    # Return the list of error times and the average time
    return error_times, average_time
logs = [
    '2022-01-01 12:34:56 ERROR: Something went wrong',
    '2022-01-01 13:45:56 ERROR: Something else went wrong',
    '2022-01-01 14:56:56 INFO: Everything is fine',
    '2022-01-01 15:07:56 ERROR: Something went wrong again',
    '2022-01-01 16:18:56 ERROR: Something went wrong for the third time',
]