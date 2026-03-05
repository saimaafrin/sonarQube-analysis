
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
    
    # Create a bar plot for the average grades
    avg_plot = avg_grades.plot(kind='bar', title='Course-wise Average Grades')
    
    # Create a bar plot for the passing grade counts
    passing_plot = passing_counts.plot(kind='bar', title='Course-wise Passing Grade Counts')
    
    # Combine the plots into a single figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    avg_plot.figure = fig
    passing_plot.figure = fig
    avg_plot.axes = axes[0]
    passing_plot.axes = axes[1]
    
    return df, axes[0]