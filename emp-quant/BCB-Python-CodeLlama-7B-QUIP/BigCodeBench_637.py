
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Generate a random list of grades for a group of students
    grades = np.random.randint(0, 100, num_students)

    # Create a Pandas DataFrame with the grades
    df = pd.DataFrame({'grades': grades})

    # Calculate the average grade in each course
    course_avg = df.groupby('grades').mean()

    # Calculate the number of students with a passing grade (>= 60)
    passing_count = df[df['grades'] >= 60].count()

    # Visualize the results with a bar plot
    fig, ax = plt.subplots()
    ax.bar(course_avg.index, course_avg.values, label='Average Grade')
    ax.bar(passing_count.index, passing_count.values, label='Passing Grade Count')
    ax.set_xlabel('Course')
    ax.set_ylabel('Grade')
    ax.legend()
    plt.show()

    return df, ax