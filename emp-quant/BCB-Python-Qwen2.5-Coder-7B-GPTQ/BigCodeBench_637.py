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
    
    # Calculate the number of students with a passing grade (>= 60)
    passing_counts = (df >= 60).sum()
    
    # Combine the average grades and passing counts into a single DataFrame
    result_df = pd.DataFrame({
        'Average Grade': avg_grades,
        'Passing Count': passing_counts
    })
    
    # Create a bar plot for the course-wise average and passing grade counts
    fig, ax = plt.subplots()
    ax.bar(result_df.index, result_df['Average Grade'], label='Average Grade')
    ax.bar(result_df.index, result_df['Passing Count'], label='Passing Count', bottom=result_df['Average Grade'])
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()
    
    return result_df, ax