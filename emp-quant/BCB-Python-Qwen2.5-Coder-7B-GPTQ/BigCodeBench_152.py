import pandas as pd
import numpy as np
from random import randint
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']
def task_func():
    # Create a dictionary to store student grades
    grades_dict = {student: [] for student in STUDENTS}
    
    # Populate the dictionary with random grades
    for student in STUDENTS:
        for course in COURSES:
            grade = randint(0, 100)
            grades_dict[student].append(grade)
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(grades_dict)
    
    # Calculate the average grade for each student
    df['Average Grade'] = df.mean(axis=1)
    
    return df