
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    if seed is not None:
        random.seed(seed)
    
    data = {'Student': students}
    for subject in subjects:
        grades = [random.randint(50, 100) for _ in range(len(students))]
        data[subject] = grades
        data['Average Grade'] = data[subjects].mean(axis=1)
    
    df = pd.DataFrame(data)
    return df