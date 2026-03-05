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
    - n_grades: int, the number of grades to generate.
    - students: list, a list of student names.
    - grade_range: range, the range of possible grades.
    - rng_seed: int, an optional seed for the random number generator for reproducibility.
    
    Returns:
    - DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'.
    
    Raises:
    - ValueError: If the list of students is empty.
    """
    if not students:
        raise ValueError("The list of students cannot be empty.")
    
    if rng_seed is not None:
        seed(rng_seed)
    
    student_cycle = cycle(students)
    grades = [randint(*grade_range) for _ in range(n_grades)]
    
    grade_report = pd.DataFrame({
        'Student': [next(student_cycle) for _ in range(n_grades)],
        'Grade': grades
    })
    
    return grade_report