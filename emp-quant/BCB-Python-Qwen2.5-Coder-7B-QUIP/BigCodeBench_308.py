
import pandas as pd
from statistics import mean
import random

# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def task_func(additional_fields = []):
    # Generate random grades for each student in each subject
    grades = {}
    for student in STUDENTS:
        grades[student] = {field: random.randint(0, 100) for field in FIELDS}

    # Create a DataFrame from the grades
    df = pd.DataFrame(grades).transpose()

    # Calculate the average grade for each student
    df['Average'] = df.mean(axis=1)

    # Calculate the average grade for each subject
    subject_averages = df.mean()

    # Add the average grade for each subject to the DataFrame
    df['Average'] = df['Average'].append(pd.Series(subject_averages, name='Average'))

    # Set the index to the subjects
    df = df.set_index('Average')

    # Add the average grade for each student to the DataFrame
    df['Average'] = df['Average'].append(df['Average'].mean(), name='Average')

    # Set the index to the students
    df = df.set_index('Average')

    # Return the DataFrame
    return df