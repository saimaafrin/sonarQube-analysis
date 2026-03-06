
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
               ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer")
    
    rng = np.random.default_rng(rng_seed)
    
    country_samples = rng.choice(countries, size=num_samples)
    age_samples = rng.choice(ages, size=num_samples)
    gender_labels = LabelEncoder().fit_transform(genders)
    gender_samples = rng.choice(gender_labels, size=num_samples)
    
    demographics_data = {
        'Country': country_samples,
        'Age': age_samples,
        'Gender': gender_samples
    }
    
    return pd.DataFrame(demographics_data)