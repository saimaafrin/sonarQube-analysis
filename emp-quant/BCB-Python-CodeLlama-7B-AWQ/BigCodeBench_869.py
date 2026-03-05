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

    Args:
        n_grades (int): The number of grades to generate.
        students (list, optional): A list of students' names. Defaults to ['Alice', 'Bob', 'Charlie', 'David', 'Eve'].
        grade_range (range, optional): A range of grades. Defaults to range(1, 11).
        rng_seed (int, optional): A seed for reproducible random numbers. Defaults to None.

    Returns:
        DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'. Each row represents a student's grade.

    Raises:
        ValueError: If list of students is empty.
    """
    if not students:
        raise ValueError("List of students is empty.")

    # Set random seed if provided
    if rng_seed:
        seed(rng_seed)

    # Generate random grades
    grades = [randint(min(grade_range), max(grade_range)) for _ in range(n_grades)]

    # Create DataFrame with student and grade columns
    df = pd.DataFrame({'Student': students, 'Grade': grades})

    return df