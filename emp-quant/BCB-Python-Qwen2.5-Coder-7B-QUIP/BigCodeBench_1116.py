
import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    # Extract ages for employees in department "EMP$$"
    ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for employee in dict1['EMP$$']]
    
    # Calculate mean
    mean_age = statistics.mean(ages)
    
    # Calculate median
    median_age = statistics.median(ages)
    
    # Calculate mode(s)
    mode_ages = statistics.mode(ages)
    
    # Return tuple of mean, median, and mode(s)
    return (mean_age, median_age, mode_ages)