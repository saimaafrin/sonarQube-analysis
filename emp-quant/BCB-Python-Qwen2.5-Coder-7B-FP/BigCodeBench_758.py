import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    # Check if num_samples is an integer
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")
    
    # Initialize the random number generator with the provided seed
    rng = np.random.default_rng(rng_seed)
    
    # Sample countries, ages, and genders
    sampled_countries = rng.choice(countries, size=num_samples)
    sampled_ages = rng.choice(ages, size=num_samples)
    sampled_genders = rng.choice(genders, size=num_samples)
    
    # Encode genders using LabelEncoder
    label_encoder = LabelEncoder()
    encoded_genders = label_encoder.fit_transform(sampled_genders)
    
    # Create a DataFrame with the sampled data
    demographics = pd.DataFrame({
        'Country': sampled_countries,
        'Age': sampled_ages,
        'Gender': encoded_genders
    })
    
    return demographics