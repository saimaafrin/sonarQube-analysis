
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
    
    country_samples = rng.choice(countries, size=num_samples)
    age_samples = rng.choice(ages, size=num_samples)
    gender_samples = rng.choice(genders, size=num_samples)
    
    label_encoder = LabelEncoder()
    gender_encoded = label_encoder.fit_transform(gender_samples)
    
    demographics = pd.DataFrame({
        'Country': country_samples,
        'Age': age_samples,
        'Gender': gender_encoded
    })
    
    return demographics