
import pandas as pd
from statistics import mean
import random
# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]
def task_func(additional_fields = []):
    # Generate random grades for each student
    grades = {
        student: {
            field: random.randint(0, 100) for field in FIELDS
        } for student in STUDENTS
    }
    # Calculate the average grade for each subject
    avg_grades = {
        field: mean([grades[student][field] for student in STUDENTS]) for field in FIELDS
    }
    # Create the DataFrame
    df = pd.DataFrame({
        'Student': STUDENTS,
        'Physics': [grades[student]['Physics'] for student in STUDENTS],
        'Math': [grades[student]['Math'] for student in STUDENTS],
        'Chemistry': [grades[student]['Chemistry'] for student in STUDENTS],
        'Biology': [grades[student]['Biology'] for student in STUDENTS],
        'English': [grades[student]['English'] for student in STUDENTS],
        'History': [grades[student]['History'] for student in STUDENTS],
        'Average Grade': [avg_grades[field] for field in FIELDS]
    })
    return df