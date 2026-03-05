
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")

    # Create a list of tuples with the demographic data
    demographics = []
    for i in range(num_samples):
        country = np.random.choice(countries)
        age = np.random.choice(ages)
        gender = np.random.choice(genders)
        demographics.append((country, age, gender))

    # Create a DataFrame with the demographic data
    df = pd.DataFrame(demographics, columns=['Country', 'Age', 'Gender'])

    # Encode the gender column using LabelEncoder
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])

    return df