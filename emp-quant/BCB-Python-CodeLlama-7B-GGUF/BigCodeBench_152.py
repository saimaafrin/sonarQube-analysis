
import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Create a dictionary to store the grades for each student
    grades = {}
    for student in STUDENTS:
        grades[student] = {}
        for course in COURSES:
            grades[student][course] = randint(0, 100)

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(grades)

    # Calculate the average grade for each student
    df['Average'] = df.apply(lambda x: x.mean(), axis=1)

    return df