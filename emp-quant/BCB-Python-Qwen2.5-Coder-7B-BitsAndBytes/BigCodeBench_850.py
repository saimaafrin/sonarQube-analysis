
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    # Seed the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Initialize an empty list to store the data
    data = []
    
    # Loop through each student
    for _ in range(students):
        # Generate random grades for each subject
        grades = [random.randint(50, 100) for _ in range(subjects)]
        
        # Calculate the average grade
        average_grade = statistics.mean(grades)
        
        # Append the data to the list
        data.append([_, *grades, average_grade])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Student'] + [f'Subject{i+1}' for i in range(subjects)] + ['Average Grade'])
    
    return df