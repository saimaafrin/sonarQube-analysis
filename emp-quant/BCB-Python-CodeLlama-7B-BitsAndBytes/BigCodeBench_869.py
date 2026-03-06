
import pandas as pd
from itertools import cycle
from random import randint, seed

def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    if not students:
        raise ValueError("List of students is empty")

    # Set the random seed if provided
    if rng_seed:
        seed(rng_seed)

    # Create a cycle of random grades
    grades = cycle(grade_range)

    # Create a dictionary to store the student and grade pairs
    student_grades = {}

    # Assign a random grade to each student
    for student in students:
        student_grades[student] = next(grades)

    # Create a pandas DataFrame from the dictionary
    grade_report = pd.DataFrame(student_grades, columns=['Student', 'Grade'])

    return grade_report