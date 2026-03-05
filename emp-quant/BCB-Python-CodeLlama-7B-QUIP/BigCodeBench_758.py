
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")
    if rng_seed is not None:
        rng = np.random.default_rng(rng_seed)
    else:
        rng = np.random.default_rng()
    countries = LabelEncoder().fit_transform(countries)
    ages = LabelEncoder().fit_transform(ages)
    genders = LabelEncoder().fit_transform(genders)
    data = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': genders
    })
    samples = rng.choice(data, num_samples, replace=False)
    return samples