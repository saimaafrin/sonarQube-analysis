
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Generate random grades for each student
    grades = []
    for _ in range(students):
        grades.append([random.randint(0, 100) for _ in range(subjects)])

    # Calculate average grade for each student
    averages = []
    for student in grades:
        averages.append(statistics.mean(student))

    # Create DataFrame with results
    df = pd.DataFrame({
        'Student': range(1, students + 1),
        'Subject1': grades[0],
        'Subject2': grades[1],
        'Subject3': grades[2],
        'Average Grade': averages
    })

    return df