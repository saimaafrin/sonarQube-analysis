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
    # Generate random grades for each student
    if seed:
        random.seed(seed)
    grades = {student: {subject: random.randint(0, 100) for subject in subjects} for student in students}

    # Calculate the average grade for each student
    averages = {student: statistics.mean(grades[student].values()) for student in students}

    # Create a DataFrame with the results
    df = pd.DataFrame(grades, columns=['Student', 'Subject1', 'Subject2', 'Average Grade'])
    df['Average Grade'] = df['Average Grade'].astype(int)

    return df
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'English', 'Science']
seed = 42