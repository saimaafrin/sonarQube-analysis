
import pandas as pd
from statistics import mean
import random

# Constants for generating the report data
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def task_func(additional_fields = []):
    # Create a dictionary to store the grades
    grades = {student: {field: random.randint(0, 100) for field in FIELDS} for student in STUDENTS}
    
    # Create a dictionary to store the average grades for each student
    average_grades = {student: mean(grades[student].values()) for student in STUDENTS}
    
    # Create a dictionary to store the average grades for each subject
    subject_averages = {field: mean(grades[student][field] for student in STUDENTS) for field in FIELDS}
    
    # Create a DataFrame to store the grades and average grades
    df = pd.DataFrame(grades)
    df['Average Grade'] = list(average_grades.values())
    
    # Add the average grades for each subject as a new row
    df.loc['Average'] = list(subject_averages.values())
    
    return df