
import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    if num_of_students <= 0:
        raise ValueError("num_of_students must be positive")
    set_seed(seed)
    names = choice(name_list, num_of_students) if name_list else ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Harry", "Ivy", "Jane", "Kyle", "Lily", "Maya", "Nina", "Oscar", "Pete", "Queenie", "Rex", "Sarah", "Ted", "Uma", "Victor", "Wanda", "Xavier", "Yuna", "Zoe"]
    genders = choice(gender_list, num_of_students) if gender_list else ["Male", "Female"]
    ages = choice(range(age_range[0], age_range[1] + 1), num_of_students)
    scores = choice(range(score_range[0], score_range[1] + 1), num_of_students)
    return pd.DataFrame({
        "Name": names,
        "Gender": genders,
        "Age": ages,
        "Score": scores
    })