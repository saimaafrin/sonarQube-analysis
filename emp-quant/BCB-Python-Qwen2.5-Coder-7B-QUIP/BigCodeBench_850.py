
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    # Seed the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)

    # Initialize a list to hold the data for the DataFrame
    data = []

    # Generate grades for each student across the subjects
    for _ in range(students):
        grades = [random.randint(50, 100) for _ in range(len(subjects))]
        average_grade = statistics.mean(grades)
        data.append([f"Student {_}", *grades, average_grade])

    # Create the DataFrame
    df = pd.DataFrame(data, columns=['Student', *subjects, 'Average Grade'])

    return df