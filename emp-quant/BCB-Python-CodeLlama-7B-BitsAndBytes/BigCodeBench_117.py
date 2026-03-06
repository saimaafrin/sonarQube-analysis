
import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def task_func(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    if num_of_students <= 0:
        raise ValueError("Number of students must be positive")

    set_seed(seed)

    names = name_list if name_list is not None else ["John", "Jane", "Bob", "Alice"]
    genders = gender_list if gender_list is not None else ["Male", "Female"]
    ages = np.random.randint(age_range[0], age_range[1], size=num_of_students)
    scores = np.random.randint(score_range[0], score_range[1], size=num_of_students)

    data = {"Name": [choice(names) for _ in range(num_of_students)],
            "Age": ages,
            "Gender": [choice(genders) for _ in range(num_of_students)],
            "Score": scores}

    return pd.DataFrame(data)