import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    """
    Generate a demographic dataset with information about people from different countries, their age, and gender.
    Genders are encoded using sklearn LabelEncoder. Datapoints are sampled from the lists using a numpy.random.default_rng with seed: rng_seed.
    """
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")

    # Create a list of countries
    countries = np.random.default_rng(rng_seed).choice(countries, size=num_samples, replace=True)

    # Create a list of ages
    ages = np.random.default_rng(rng_seed).choice(ages, size=num_samples, replace=True)

    # Create a list of genders
    genders = np.random.default_rng(rng_seed).choice(genders, size=num_samples, replace=True)

    # Create a DataFrame with the demographics data
    demographics = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': genders
    })

    return demographics