
import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    # Extract ages from the dictionary where department is 'EMP$$'
    ages = [employee['age'] for employee in dict1.values() if employee['department'] == 'EMP$$']
    
    # Calculate mean
    mean_age = statistics.mean(ages)
    
    # Calculate median
    median_age = statistics.median(ages)
    
    # Calculate mode(s)
    mode_ages = statistics.multimode(ages)
    
    return (mean_age, median_age, mode_ages)