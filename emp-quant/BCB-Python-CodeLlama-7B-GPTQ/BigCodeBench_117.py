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
        A tuple of integers representing the range of ages to generate.
    score_range : tuple, optional
        A tuple of integers representing the range of scores to generate.

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
        raise ValueError("Number of students must be positive.")

    # Set the random seed for reproducibility
    set_seed(seed)

    # Generate random names, ages, genders, and scores
    names = np.random.choice(name_list, num_of_students)
    ages = np.random.randint(age_range[0], age_range[1], num_of_students)
    genders = np.random.choice(gender_list, num_of_students)
    scores = np.random.randint(score_range[0], score_range[1], num_of_students)

    # Create a DataFrame with the generated data
    df = pd.DataFrame({"Name": names, "Age": ages, "Gender": genders, "Score": scores})

    return df