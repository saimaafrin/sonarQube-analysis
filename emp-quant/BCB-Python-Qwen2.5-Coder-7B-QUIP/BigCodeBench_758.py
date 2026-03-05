
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
               ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")
    
    if rng_seed is not None:
        np.random.seed(rng_seed)
    
    le = LabelEncoder()
    le.fit(genders)
    genders_encoded = le.transform(genders)
    
    country_samples = np.random.choice(countries, num_samples)
    age_samples = np.random.choice(ages, num_samples)
    gender_samples = np.random.choice(genders_encoded, num_samples)
    
    demographics = pd.DataFrame({
        'Country': country_samples,
        'Age': age_samples,
        'Gender': gender_samples
    })
    
    return demographics