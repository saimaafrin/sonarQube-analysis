import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    """
    Generate a demographic dataset with information about people from different countries, their age, and gender.
    Genders are encoded using sklearn LabelEncoder.
    Datapoints are sampled from the lists using a numpy.random.default_rng with seed: rng_seed.
    """
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")

    # Create a list of unique countries
    unique_countries = np.unique(countries)

    # Create a list of unique ages
    unique_ages = np.unique(ages)

    # Create a list of unique genders
    unique_genders = np.unique(genders)

    # Create a list of tuples containing country, age, and gender
    demographics = []
    for country in unique_countries:
        for age in unique_ages:
            for gender in unique_genders:
                demographics.append((country, age, gender))

    # Shuffle the list of tuples using the given seed
    if rng_seed is not None:
        rng = np.random.default_rng(rng_seed)
        rng.shuffle(demographics)

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(demographics, columns=['Country', 'Age', 'Gender'])

    # Encode the genders using LabelEncoder
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])

    return df