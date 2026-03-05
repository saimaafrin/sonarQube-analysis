import pandas as pd
import numpy as np
from random import randint
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']
def task_func():
    # Generate random grades for each course
    grades = np.random.randint(0, 100, size=(len(STUDENTS), len(COURSES)))
    # Create a DataFrame with columns for each student's name, their grades for each course, and their average grade across all courses
    df = pd.DataFrame(grades, columns=['Student', 'Course', 'Average'])
    df['Student'] = STUDENTS
    df['Course'] = COURSES
    df['Average'] = df.mean(axis=1)
    return df