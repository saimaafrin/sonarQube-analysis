import pandas as pd
import numpy as np
from random import randint
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']
def task_func():
    """
    Generates a DataFrame containing random grades for a predefined list of students across a set of courses.
    Each student will have one grade per course and an average grade calculated across all courses.

    Returns:
    DataFrame: A pandas DataFrame with columns for each student's name, their grades for each course,
               and their average grade across all courses.

    Requirements:
    - pandas
    - numpy
    - random

    Note:
    The grades are randomly generated for each course using a uniform distribution between 0 and 100.

    Example:
    >>> random.seed(0)
    >>> grades = task_func()
    >>> print(grades[['Name', 'Average Grade']].to_string(index=False))
     Name  Average Grade
      Joe         51.875
      Amy         53.250
     Mark         53.750
     Sara         47.125
     John         55.250
    Emily         48.625
      Zoe         63.750
     Matt         54.750
    """
    # Create a DataFrame with columns for each student's name, their grades for each course, and their average grade across all courses
    grades = pd.DataFrame(columns=['Name', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science', 'Average Grade'])

    # Add a row for each student
    for student in STUDENTS:
        # Add a row for each course
        for course in COURSES:
            # Generate a random grade for the course
            grade = randint(0, 100)
            # Add the grade to the DataFrame
            grades.loc[len(grades)] = [student, grade, grade, grade, grade, grade, grade, grade, grade, grade]

    # Calculate the average grade for each student
    grades['Average Grade'] = grades.iloc[:, 1:].mean(axis=1)

    return grades