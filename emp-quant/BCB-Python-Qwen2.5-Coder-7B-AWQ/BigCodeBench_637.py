from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def task_func(num_students):
    # Generate random grades for students in multiple courses
    courses = ['Math', 'Science', 'History', 'English', 'Art']
    grades = {course: np.random.randint(50, 100, num_students) for course in courses}
    df = pd.DataFrame(grades)
    
    # Calculate average grade in each course
    avg_grades = df.mean()
    
    # Count the number of students with a passing grade (>= 60)
    passing_counts = (df >= 60).sum()
    
    # Create a new DataFrame to store the results
    result_df = pd.DataFrame({
        'Average Grade': avg_grades,
        'Passing Count': passing_counts
    })
    
    # Visualize the information using a bar plot
    fig, ax = plt.subplots()
    ax.bar(result_df.index, result_df['Average Grade'], label='Average Grade')
    ax.bar(result_df.index, result_df['Passing Count'], bottom=result_df['Average Grade'], label='Passing Count')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()
    
    return result_df, ax