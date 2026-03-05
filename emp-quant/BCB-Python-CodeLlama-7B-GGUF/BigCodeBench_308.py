
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
        grades[student] = {}
        for field in FIELDS:
            grades[student][field] = random.randint(0, 100)

    # Create a DataFrame with the grades and average grades
    df = pd.DataFrame(grades)
    df['Average'] = df.apply(lambda x: mean(x), axis=1)

    # Add the average grade per subject
    for field in FIELDS:
        df[field + ' Average'] = df[field].mean()

    return df

# Generate the report
df = task_func()
print(df)