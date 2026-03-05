
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
        raise ValueError("List of students is empty.")
    
    if rng_seed is not None:
        seed(rng_seed)
    
    student_cycle = cycle(students)
    grades = [randint(grade_range.start, grade_range.stop) for _ in range(n_grades)]
    
    grade_report = pd.DataFrame({'Student': [next(student_cycle) for _ in range(n_grades)],
                                'Grade': grades})
    
    return grade_report