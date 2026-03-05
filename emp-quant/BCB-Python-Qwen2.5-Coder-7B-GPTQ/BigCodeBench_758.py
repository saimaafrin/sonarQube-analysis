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
    
    # Encode genders using LabelEncoder
    label_encoder = LabelEncoder()
    encoded_genders = label_encoder.fit_transform(genders)
    
    # Sample data
    country_samples = rng.choice(countries, size=num_samples)
    age_samples = rng.choice(ages, size=num_samples)
    gender_samples = rng.choice(encoded_genders, size=num_samples)
    
    # Create DataFrame
    demographics = pd.DataFrame({
        'Country': country_samples,
        'Age': age_samples,
        'Gender': gender_samples
    })
    
    return demographics