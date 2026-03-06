
import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    # Generate random ages for each employee within the range
    employee_ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for _ in range(len(dict1))]

    # Calculate mean, median, and mode(s) of employee ages
    mean = statistics.mean(employee_ages)
    median = statistics.median(employee_ages)
    mode = statistics.mode(employee_ages)

    # Return a tuple of mean, median, and a list of mode(s) of employee ages
    return (mean, median, [mode])