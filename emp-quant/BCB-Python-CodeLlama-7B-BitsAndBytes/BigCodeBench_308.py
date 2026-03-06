
import pandas as pd
from statistics import mean
import random

# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def task_func(additional_fields = []):
    # Generate random grades for each student and subject
    grades = {}
    for student in STUDENTS:
        grades[student] = {}
        for field in FIELDS:
            grades[student][field] = random.randint(0, 100)

    # Calculate the average grade for each subject
    average_grades = {}
    for field in FIELDS:
        average_grades[field] = mean(grades[student][field] for student in STUDENTS)

    # Create a DataFrame with the grades and average grades
    df = pd.DataFrame(grades, columns=FIELDS)
    df['Average Grade'] = average_grades

    return df

# Generate the report
df = task_func()
print(df)