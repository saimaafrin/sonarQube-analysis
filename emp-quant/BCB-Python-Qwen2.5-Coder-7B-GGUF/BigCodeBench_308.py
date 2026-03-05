
import pandas as pd
from statistics import mean
import random

# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def task_func(additional_fields = []):
    # Create a dictionary to store the grades
    grades = {student: {field: random.randint(0, 100) for field in FIELDS} for student in STUDENTS}
    
    # Create a dictionary to store the average grades per student
    average_grades_per_student = {student: mean(grades[student].values()) for student in STUDENTS}
    
    # Create a dictionary to store the average grades per subject
    average_grades_per_subject = {field: mean(grades[student][field] for student in STUDENTS) for field in FIELDS}
    
    # Create a DataFrame to store the grades and average grades
    df = pd.DataFrame(grades).T
    df['Average Grade'] = df.mean(axis=1)
    
    # Add the average grades per subject as a new row
    df.loc['Average'] = pd.Series(average_grades_per_subject, name='Average')
    
    return df