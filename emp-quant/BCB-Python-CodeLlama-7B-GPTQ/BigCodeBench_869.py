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
        n_grades (int): Number of grades to generate.
        students (list, optional): List of students to generate grades for. Defaults to ['Alice', 'Bob', 'Charlie', 'David', 'Eve'].
        grade_range (range, optional): Range of grades to generate. Defaults to range(1, 11).
        rng_seed (int, optional): Random seed for reproducibility. Defaults to None.

    Raises:
        ValueError: If list of students is empty.

    Returns:
        DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'. Each row represents a student's grade.
    """
    if not students:
        raise ValueError("List of students is empty.")

    # Generate random grades
    if rng_seed:
        seed(rng_seed)
    grades = [randint(min(grade_range), max(grade_range)) for _ in range(n_grades)]

    # Create DataFrame
    df = pd.DataFrame({
        'Student': students,
        'Grade': grades
    })

    return df