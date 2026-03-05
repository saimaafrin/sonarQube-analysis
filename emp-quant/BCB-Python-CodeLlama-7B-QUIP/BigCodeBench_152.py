
import pandas as pd
import numpy as np
from random import randint
# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']
def task_func():
    # Generate grades for each student
    grades = []
    for student in STUDENTS:
        grades.append([randint(0, 100) for _ in range(len(COURSES))])
    # Calculate average grade for each student
    averages = [np.mean(grades[i]) for i in range(len(STUDENTS))]
    # Create DataFrame
    df = pd.DataFrame({'Name': STUDENTS, 'Grades': grades, 'Average': averages})
    return df