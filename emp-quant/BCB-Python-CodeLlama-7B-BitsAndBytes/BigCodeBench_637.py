
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Generate random grades for each course
    course_1_grades = np.random.randint(0, 100, size=num_students)
    course_2_grades = np.random.randint(0, 100, size=num_students)
    course_3_grades = np.random.randint(0, 100, size=num_students)

    # Create a DataFrame with the grades
    df = pd.DataFrame({
        'Course 1': course_1_grades,
        'Course 2': course_2_grades,
        'Course 3': course_3_grades
    })

    # Calculate the average grade for each course
    course_1_avg = df['Course 1'].mean()
    course_2_avg = df['Course 2'].mean()
    course_3_avg = df['Course 3'].mean()

    # Calculate the number of students with a passing grade for each course
    course_1_passing = (df['Course 1'] >= 60).sum()
    course_2_passing = (df['Course 2'] >= 60).sum()
    course_3_passing = (df['Course 3'] >= 60).sum()

    # Create a bar plot with the average grade and passing grade counts for each course
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3], [course_1_avg, course_2_avg, course_3_avg], label='Average Grade')
    ax.bar([1, 2, 3], [course_1_passing, course_2_passing, course_3_passing], label='Passing Grade Count')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()

    return (df, ax)