from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def task_func(num_students):
    # Generate random grades for a group of students in multiple courses
    num_courses = 3
    course_grades = np.random.randint(0, 100, size=(num_students, num_courses))

    # Calculate average grade in each course and number of passing grades
    course_means = course_grades.mean(axis=0)
    passing_counts = (course_grades >= 60).sum(axis=0)

    # Create a DataFrame with the results
    df = pd.DataFrame({'Course': range(1, num_courses + 1),
                       'Average Grade': course_means,
                       'Passing Count': passing_counts})

    # Visualize the results using a bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Course'], df['Average Grade'], label='Average Grade')
    ax.bar(df['Course'], df['Passing Count'], bottom=df['Average Grade'], label='Passing Count')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Course')
    ax.set_ylabel('Grade')
    ax.legend()

    return df, ax
num_students = 100