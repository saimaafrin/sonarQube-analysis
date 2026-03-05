from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def task_func(num_students):
    # Generate random grades for a group of students in multiple courses
    courses = ['Math', 'Science', 'English', 'History']
    grades = {course: np.random.randint(0, 100, num_students) for course in courses}

    # Calculate average grade in each course and number of passing grades
    course_avgs = {course: grades[course].mean() for course in courses}
    passing_grades = {course: (grades[course] >= 60).sum() for course in courses}

    # Create a Pandas DataFrame with the results
    df = pd.DataFrame(data=passing_grades, index=courses, columns=['Passing Grades'])
    df['Average Grade'] = course_avgs

    # Create a bar plot with the results
    fig, ax = plt.subplots()
    ax.bar(df.index, df['Passing Grades'], label='Passing Grades')
    ax.bar(df.index, df['Average Grade'], label='Average Grade')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.set_xlabel('Course')
    ax.set_ylabel('Count')
    ax.legend()

    return df, ax
num_students = 10