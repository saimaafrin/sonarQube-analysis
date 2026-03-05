
import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    # Create a dictionary to store the grades
    grades_dict = {student: {course: randint(0, 100) for course in COURSES} for student in STUDENTS}
    
    # Calculate the average grade for each student
    for student in STUDENTS:
        grades_dict[student]['Average'] = np.mean(list(grades_dict[student].values()))
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(grades_dict, orient='index')
    
    return df