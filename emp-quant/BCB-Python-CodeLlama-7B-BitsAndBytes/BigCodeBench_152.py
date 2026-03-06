
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

    # Calculate the average grade for each student
    average_grades = {}
    for student in STUDENTS:
        average_grades[student] = np.mean(list(grades[student].values()))

    # Create a DataFrame with the grades and average grades
    df = pd.DataFrame(grades, index=STUDENTS)
    df['Average'] = average_grades

    return df

# Call the function and print the output
df = task_func()
print(df)