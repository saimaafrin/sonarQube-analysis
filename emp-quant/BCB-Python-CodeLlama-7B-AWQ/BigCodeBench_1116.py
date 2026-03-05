import random
import statistics
AGE_RANGE = (22, 60)
def task_func(dict1):
    """
    Calculate the mean, median, and mode(s) of the age of the employees in the department "EMP$$."
    Generate random ages for each employee within the range [22, 60].
    """
    # Generate random ages for each employee
    employee_ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for _ in range(len(dict1))]

    # Calculate mean, median, and mode(s) of employee ages
    mean = statistics.mean(employee_ages)
    median = statistics.median(employee_ages)
    mode = statistics.mode(employee_ages)

    # Return tuple of mean, median, and mode(s) of employee ages
    return (mean, median, mode)
dict1 = {
    "EMP1": {"age": 25},
    "EMP2": {"age": 30},
    "EMP3": {"age": 35},
    "EMP4": {"age": 40},
    "EMP5": {"age": 45},
    "EMP6": {"age": 50},
    "EMP7": {"age": 55},
    "EMP8": {"age": 60},
}