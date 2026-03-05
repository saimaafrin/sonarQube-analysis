import pandas as pd
from statistics import mean
import random
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]
def task_func(additional_fields = []):
    # Generate random grades for each student in each subject
    grades = {student: {field: random.randint(0, 100) for field in FIELDS} for student in STUDENTS}

    # Create a DataFrame with the grades and average grades
    df = pd.DataFrame(grades)
    df['Average'] = df.apply(lambda row: mean(row[FIELDS]), axis=1)

    # Add the average grade per subject
    df['Average Grade'] = df.apply(lambda row: mean(row[FIELDS]), axis=0)

    return df