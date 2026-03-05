
import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    """
    Generate a Pandas DataFrame with randomized student data.

    Parameters:
    num_of_students (int): The total number of students to generate.
    seed (int): The random seed for reproducible results.
    name_list (list): A list of names to choose from. Defaults to ['Alice', 'Bob', 'Charlie', 'David', 'Eve'].
    gender_list (list): A list of genders to choose from. Defaults to ['Male', 'Female'].
    age_range (tuple): A tuple of two integers representing the range of ages (inclusive). Defaults to (15, 20).
    score_range (tuple): A tuple of two integers representing the range of scores (inclusive). Defaults to (50, 100).

    Returns:
    pandas.DataFrame: A DataFrame object with columns ['Name', 'Age', 'Gender', 'Score'].
    """
    if num_of_students <= 0:
        raise ValueError("num_of_students must be positive")

    if name_list is None:
        name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    if gender_list is None:
        gender_list = ['Male', 'Female']

    set_seed(seed)

    data = {
        'Name': [choice(name_list) for _ in range(num_of_students)],
        'Age': [np.random.randint(age_range[0], age_range[1] + 1) for _ in range(num_of_students)],
        'Gender': [choice(gender_list) for _ in range(num_of_students)],
        'Score': [np.random.randint(score_range[0], score_range[1] + 1) for _ in range(num_of_students)]
    }

    return pd.DataFrame(data)