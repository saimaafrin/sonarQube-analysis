import random
import statistics
def task_func(dict1):
    # Extract ages of employees in the department "EMP$$"
    ages = [employee['age'] for employee in dict1.values() if employee['department'] == 'EMP$$']
    
    # Calculate mean
    mean_age = statistics.mean(ages)
    
    # Calculate median
    median_age = statistics.median(ages)
    
    # Calculate mode(s)
    mode_ages = statistics.multimode(ages)
    
    return (mean_age, median_age, mode_ages)