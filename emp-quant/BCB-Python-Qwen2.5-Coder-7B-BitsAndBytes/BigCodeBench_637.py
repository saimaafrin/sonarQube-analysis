
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Define the courses
    courses = ['Math', 'Science', 'History', 'English']
    
    # Generate random grades for each student in each course
    data = {course: [np.random.randint(50, 100) for _ in range(num_students)] for course in courses}
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Calculate the average grade in each course
    avg_grades = df.mean()
    
    # Count the number of students with a passing grade (>= 60) in each course
    passing_counts = (df >= 60).sum()
    
    # Combine the average grades and passing counts into a single DataFrame
    result_df = pd.DataFrame({'Average Grade': avg_grades, 'Passing Count': passing_counts})
    
    # Visualize the information using a bar plot
    fig, ax = plt.subplots()
    result_df.plot(kind='bar', ax=ax)
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Courses')
    ax.set_ylabel('Values')
    
    return result_df, ax