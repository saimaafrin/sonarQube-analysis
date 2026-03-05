
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Define the courses
    courses = ['Math', 'Science', 'History', 'English', 'Art']
    
    # Generate random grades for each student in each course
    data = {course: sample(range(50, 101), num_students) for course in courses}
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Calculate the average grade in each course
    average_grades = df.mean()
    
    # Calculate the number of students with a passing grade (>= 60)
    passing_counts = (df >= 60).sum()
    
    # Combine the average grades and passing counts into a single DataFrame
    result_df = pd.DataFrame({
        'Average Grade': average_grades,
        'Passing Count': passing_counts
    })
    
    # Create a bar plot
    fig, ax = plt.subplots()
    result_df.plot(kind='bar', ax=ax)
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Courses')
    ax.set_ylabel('Values')
    
    return result_df, ax