
import pandas as pd
import numpy as np
from random import randint
# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Generate random grades for each student across each course
    grades = {}
    for student in STUDENTS:
        grades[student] = {course: randint(0, 100) for course in COURSES}
    
    # Create a DataFrame from the grades
    df = pd.DataFrame(grades)
    
    # Calculate the average grade for each student
    df['Average Grade'] = df.mean(axis=1)
    
    # Return the DataFrame
    return df