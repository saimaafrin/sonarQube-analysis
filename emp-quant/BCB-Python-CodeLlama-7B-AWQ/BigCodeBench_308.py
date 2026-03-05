import pandas as pd
from statistics import mean
import random
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]
def task_func(additional_fields = []):
    # Generate random grades for each student in each subject
    grades = {}
    for student in STUDENTS:
        grades[student] = {}
        for field in FIELDS:
            grades[student][field] = random.randint(0, 100)

    # Calculate the average grade for each subject
    subject_averages = {}
    for field in FIELDS:
        subject_averages[field] = mean(grades[student][field] for student in STUDENTS)

    # Create a DataFrame with the grades and averages
    df = pd.DataFrame(grades, columns=FIELDS)
    df['Average'] = df.mean(axis=1)
    df['Average Grade'] = subject_averages

    return df