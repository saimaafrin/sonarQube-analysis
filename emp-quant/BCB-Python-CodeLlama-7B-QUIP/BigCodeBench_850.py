
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    if seed:
        random.seed(seed)
    grades = []
    for student in students:
        grades.append(random.randint(0, 100))
    grades = pd.DataFrame(grades, columns=['Student', 'Subject1', 'Subject2', 'Average Grade'])
    grades['Average Grade'] = grades.mean(axis=1)
    return grades