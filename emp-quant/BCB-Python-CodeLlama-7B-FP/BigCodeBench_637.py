from random import sample
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def task_func(num_students):
    # Generate random grades for students in multiple courses
    course_grades = {
        'course1': np.random.randint(0, 100, num_students),
        'course2': np.random.randint(0, 100, num_students),
        'course3': np.random.randint(0, 100, num_students),
    }

    # Calculate average grade in each course and number of passing grades
    course_avg = {course: np.mean(grades) for course, grades in course_grades.items()}
    course_pass = {course: (grades >= 60).sum() for course, grades in course_grades.items()}

    # Create DataFrame with course-wise average and passing grade counts
    df = pd.DataFrame({
        'Course': list(course_avg.keys()),
        'Average Grade': list(course_avg.values()),
        'Passing Grades': list(course_pass.values()),
    })

    # Visualize data with bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Course'], df['Average Grade'], label='Average Grade')
    ax.bar(df['Course'], df['Passing Grades'], bottom=df['Average Grade'], label='Passing Grades')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()

    return df, ax