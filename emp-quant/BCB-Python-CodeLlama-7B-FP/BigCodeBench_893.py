import re
from datetime import time
def task_func(logs: list):
    """
    Analyze the given list of logs for the occurrence of errors and calculate the average time of occurrence of errors.
    :param logs: A list of logs
    :return: A list of times when errors occurred and the average time of occurrence of these errors
    """
    error_times = []
    for log in logs:
        match = re.search(r"error", log)
        if match:
            error_times.append(time.fromisoformat(log.split(" ")[1]))
    if error_times:
        return error_times, sum(error_times) / len(error_times)
    else:
        return [], None
logs = [
    "2022-01-01 12:00:00 error",
    "2022-01-01 13:00:00 error",
    "2022-01-01 14:00:00 warning",
    "2022-01-01 15:00:00 error",
    "2022-01-01 16:00:00 warning",
    "2022-01-01 17:00:00 error",
    "2022-01-01 18:00:00 warning",
    "2022-01-01 19:00:00 error",
    "2022-01-01 20:00:00 warning",
    "2022-01-01 21:00:00 error",
    "2022-01-01 22:00:00 warning",
    "2022-01-01 23:00:00 error",
]