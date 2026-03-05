
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
        raise ValueError("The list of students cannot be empty.")
    
    if rng_seed is not None:
        seed(rng_seed)
    
    student_cycle = cycle(students)
    grades = [randint(*grade_range) for _ in range(n_grades)]
    student_names = [next(student_cycle) for _ in range(n_grades)]
    
    grade_report = pd.DataFrame({'Student': student_names, 'Grade': grades})
    return grade_report