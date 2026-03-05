import pandas as pd
import numpy as np
from random import randint
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']
def task_func():
    # Generate random grades for each course
    grades = np.random.randint(0, 101, size=(len(STUDENTS), len(COURSES)))

    # Create a DataFrame with grades and average grades
    df = pd.DataFrame(grades, columns=COURSES)
    df['Average'] = df.mean(axis=1)

    # Add student names to the DataFrame
    df['Student'] = STUDENTS

    return df