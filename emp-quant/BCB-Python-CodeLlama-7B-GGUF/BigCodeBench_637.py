
from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def task_func(num_students):
    # Generate random grades for each course
    course_1_grades = np.random.randint(0, 100, num_students)
    course_2_grades = np.random.randint(0, 100, num_students)
    course_3_grades = np.random.randint(0, 100, num_students)

    # Create a DataFrame with the grades
    grades_df = pd.DataFrame({
        'Course 1': course_1_grades,
        'Course 2': course_2_grades,
        'Course 3': course_3_grades
    })

    # Calculate the average grade in each course
    course_1_avg = grades_df['Course 1'].mean()
    course_2_avg = grades_df['Course 2'].mean()
    course_3_avg = grades_df['Course 3'].mean()

    # Calculate the number of students with a passing grade in each course
    course_1_passing = (grades_df['Course 1'] >= 60).sum()
    course_2_passing = (grades_df['Course 2'] >= 60).sum()
    course_3_passing = (grades_df['Course 3'] >= 60).sum()

    # Create a bar plot with the average grade and passing grade counts
    fig, ax = plt.subplots()
    ax.bar(['Course 1', 'Course 2', 'Course 3'], [course_1_avg, course_2_avg, course_3_avg], color='#3399ff')
    ax.bar(['Course 1', 'Course 2', 'Course 3'], [course_1_passing, course_2_passing, course_3_passing], color='#ff9933')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Course')
    ax.set_ylabel('Grade')
    ax.set_xticks(['Course 1', 'Course 2', 'Course 3'])
    ax.set_xticklabels(['Course 1', 'Course 2', 'Course 3'])

    return grades_df, ax