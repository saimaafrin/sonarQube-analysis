from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def task_func(num_students):
    # Define the courses
    courses = ['Math', 'Science', 'History', 'English', 'Art']
    
    # Generate random grades for each student in each course
    grades = {course: np.random.randint(50, 100, num_students) for course in courses}
    
    # Create a DataFrame from the grades
    df = pd.DataFrame(grades)
    
    # Calculate the average grade in each course
    avg_grades = df.mean()
    
    # Calculate the number of students with a passing grade (>= 60) in each course
    passing_counts = (df >= 60).sum()
    
    # Create a bar plot for the average grades and passing counts
    fig, ax = plt.subplots()
    ax.bar(courses, avg_grades, label='Average Grade')
    ax.bar(courses, passing_counts, bottom=avg_grades, label='Passing Count')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()
    
    # Return the DataFrame and the Axes object
    return df, ax