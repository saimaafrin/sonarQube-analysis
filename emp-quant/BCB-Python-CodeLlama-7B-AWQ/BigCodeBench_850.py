import pandas as pd
import statistics
import random
def task_func(students, subjects, seed=None):
    """
    Create a grade report for a list of students across various subjects.
    Each student's grades are randomly generated, and the report includes the average grade for each student.
    The randomness is seeded for reproducibility if a seed is provided.
    The function should output with:
        DataFrame: A pandas DataFrame containing each student's grades across the subjects and their average grade.
        Columns are ['Student', 'Subject1', 'Subject2', ..., 'Average Grade'].
    """
    # Set random seed if provided
    if seed:
        random.seed(seed)

    # Create a list of grades for each subject
    grades = []
    for subject in subjects:
        grades.append([random.randint(0, 100) for _ in range(students)])

    # Create a DataFrame with the grades and average grade for each student
    df = pd.DataFrame(grades, columns=['Subject1', 'Subject2', ..., 'Average Grade'])
    df['Student'] = df.index
    df['Average Grade'] = df.mean(axis=1)

    return df