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
    if seed is not None:
        random.seed(seed)

    # Generate random grades for each student
    grades = []
    for student in students:
        student_grades = []
        for subject in subjects:
            student_grades.append(random.randint(0, 100))
        grades.append(student_grades)

    # Calculate average grades for each student
    averages = []
    for student_grades in grades:
        averages.append(statistics.mean(student_grades))

    # Create DataFrame with grades and averages
    df = pd.DataFrame(grades, columns=['Student', 'Subject1', 'Subject2', 'Average Grade'])
    df['Average Grade'] = averages

    return df