
import pandas as pd
from statistics import mean
import random

# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def task_func(additional_fields=[]):
    # Create a dictionary to store the grades
    grades = {field: {} for field in FIELDS}
    
    # Populate the grades dictionary with random values
    for student in STUDENTS:
        for field in FIELDS:
            grades[field][student] = random.randint(0, 100)
    
    # Calculate the average grade for each student
    student_averages = {}
    for student in STUDENTS:
        student_grades = [grades[field][student] for field in FIELDS]
        student_averages[student] = mean(student_grades)
    
    # Calculate the average grade for each subject
    field_averages = {field: mean([grades[field][student] for student in STUDENTS]) for field in FIELDS}
    
    # Create a DataFrame to store the grades and averages
    df = pd.DataFrame(grades)
    
    # Add the average grades for each student as a new row
    df.loc['Average'] = student_averages
    
    # Add the average grades for each subject as a new column
    df['Average Grade'] = field_averages
    
    return df