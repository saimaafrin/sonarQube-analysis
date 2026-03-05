import pandas as pd
import numpy as np
from random import choice, seed as set_seed
def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    """
    Generates a Pandas DataFrame with randomized student data.
    
    Parameters:
    - num_of_students (int): The total number of students to generate.
    - seed (int): The seed for the random number generator for reproducibility.
    - name_list (list): A list of names to randomly select from. Defaults to a predefined list.
    - gender_list (list): A list of genders to randomly select from. Defaults to a predefined list.
    - age_range (tuple): A tuple of two integers representing the range of ages (inclusive). Defaults to (15, 20).
    - score_range (tuple): A tuple of two integers representing the range of scores (inclusive). Defaults to (50, 100).
    
    Returns:
    - pandas.DataFrame: A DataFrame object with columns ['Name', 'Age', 'Gender', 'Score'].
    
    Raises:
    - ValueError: If num_of_students is non-positive.
    """
    if num_of_students <= 0:
        raise ValueError("num_of_students must be a positive integer.")
    
    # Set the seed for reproducibility
    set_seed(seed)
    
    # Default name and gender lists if not provided
    if name_list is None:
        name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    if gender_list is None:
        gender_list = ['Male', 'Female']
    
    # Generate data
    names = [choice(name_list) for _ in range(num_of_students)]
    ages = [np.random.randint(age_range[0], age_range[1] + 1) for _ in range(num_of_students)]
    genders = [choice(gender_list) for _ in range(num_of_students)]
    scores = [np.random.randint(score_range[0], score_range[1] + 1) for _ in range(num_of_students)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Name': names,
        'Age': ages,
        'Gender': genders,
        'Score': scores
    })
    
    return df