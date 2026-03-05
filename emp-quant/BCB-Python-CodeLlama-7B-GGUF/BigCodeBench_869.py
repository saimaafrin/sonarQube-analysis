
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

    if rng_seed:
        seed(rng_seed)

    grades = cycle(grade_range)
    grade_report = pd.DataFrame(
        {
            "Student": students,
            "Grade": [next(grades) for _ in range(n_grades)]
        }
    )

    return grade_report

grade_report = task_func(5, rng_seed=12)
print(grade_report)