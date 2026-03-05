
import random
import statistics
# Constants
AGE_RANGE = (22, 60)
def task_func(dict1):
    # Generate random ages for each employee within the range
    ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for i in range(len(dict1))
    # Calculate mean, median, and mode(s) of employee ages
    mean = statistics.mean(ages)
    median = statistics.median(ages)
    mode = statistics.mode(ages)
    return (mean, median, mode)