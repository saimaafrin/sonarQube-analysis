import pandas as pd
from itertools import cycle
from random import randint, seed
def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    """
    Generates a grade report for a specified number of grades.

    Parameters:
    n_grades (int): The number of grades to generate.
    students (list): A list of student names.
    grade_range (range): A range of possible grades.
    rng_seed (int): A seed for the random number generator to make the results reproducible.

    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'.
    """
    if not students:
        raise ValueError("The list of students is empty.")
    
    if rng_seed is not None:
        seed(rng_seed)
    
    student_cycle = cycle(students)
    grades = [randint(*grade_range) for _ in range(n_grades)]
    
    grade_report = pd.DataFrame({
        'Student': [next(student_cycle) for _ in range(n_grades)],
        'Grade': grades
    })
    
    return grade_report