
import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Create a dictionary to store the data
    data = {student: [] for student in STUDENTS}
    
    # Populate the dictionary with random grades
    for student in STUDENTS:
        for _ in range(len(COURSES)):
            grade = randint(0, 100)
            data[student].append(grade)
    
    # Calculate the average grade for each student
    for student in STUDENTS:
        data[student].append(np.mean(data[student]))
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data)
    
    # Set the index to be the student names
    df.index = STUDENTS
    
    # Rename the last column to 'Average'
    df.columns = COURSES + ['Average']
    
    return df