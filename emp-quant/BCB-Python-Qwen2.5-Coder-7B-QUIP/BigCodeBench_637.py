
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Define the list of courses
    courses = ['Math', 'Science', 'History', 'English', 'Art']
    
    # Generate a list of student grades for each course
    grades = {}
    for course in courses:
        grades[course] = np.random.randint(50, 100, num_students)
    
    # Create a DataFrame from the grades dictionary
    df = pd.DataFrame(grades)
    
    # Calculate the average grade in each course
    avg_grades = df.mean()
    
    # Calculate the number of students with a passing grade (>= 60) in each course
    passing_grades = df.apply(lambda x: (x >= 60).sum(), axis=1)
    
    # Create a bar plot with title 'Course-wise Average and Passing Grade Counts'
    fig, ax = plt.subplots()
    ax.bar(courses, avg_grades, label='Average Grade')
    ax.bar(courses, passing_grades, bottom=avg_grades, label='Passing Grades')
    ax.set_xlabel('Courses')
    ax.set_ylabel('Count')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()
    
    # Return the DataFrame and the Axes object
    return df, ax