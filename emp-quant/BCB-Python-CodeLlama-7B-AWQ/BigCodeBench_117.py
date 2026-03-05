import pandas as pd
import numpy as np
from random import choice, seed as set_seed
def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    """
    Generate a Pandas DataFrame with randomized student data.

    Parameters
    ----------
    num_of_students : int
        The total number of students to generate.
    seed : int, optional
        The random seed to use for reproducibility.
    name_list : list, optional
        A list of names to select from randomly.
    gender_list : list, optional
        A list of genders to select from randomly.
    age_range : tuple, optional
        A tuple of two integers representing the minimum and maximum age range.
    score_range : tuple, optional
        A tuple of two integers representing the minimum and maximum score range.

    Returns
    -------
    pandas.DataFrame
        A DataFrame object with columns ['Name', 'Age', 'Gender', 'Score'], containing
        randomly generated data for the specified number of students. Names and genders are randomly selected
        from the provided lists (or defaults). Ages and scores are randomly generated within the specified ranges.

    Raises
    ------
    ValueError
        If num_of_students is non-positive.
    """
    if num_of_students <= 0:
        raise ValueError("Number of students must be positive")

    # Set the random seed for reproducibility
    set_seed(seed)

    # Create a list of names if not provided
    if name_list is None:
        name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

    # Create a list of genders if not provided
    if gender_list is None:
        gender_list = ["Male", "Female"]

    # Create a list of ages if not provided
    if age_range is None:
        age_range = (15, 20)

    # Create a list of scores if not provided
    if score_range is None:
        score_range = (50, 100)

    # Create a DataFrame with the specified number of rows
    df = pd.DataFrame(index=range(num_of_students), columns=["Name", "Age", "Gender", "Score"])

    # Fill in the DataFrame with random data
    for i in range(num_of_students):
        df.loc[i, "Name"] = choice(name_list)
        df.loc[i, "Age"] = np.random.randint(age_range[0], age_range[1])
        df.loc[i, "Gender"] = choice(gender_list)
        df.loc[i, "Score"] = np.random.randint(score_range[0], score_range[1])

    return df