import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    """
    Generates a demographic dataset with information about people from different countries, their age, and gender.
    
    Parameters:
    - num_samples (int): The number of samples to generate.
    - countries (list): A list of country names.
    - ages (numpy.ndarray): An array of ages.
    - genders (list): A list of gender names.
    - rng_seed (int): The seed for the random number generator.
    
    Returns:
    - DataFrame: A pandas DataFrame with the demographics data.
    """
    # Validate input
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer.")
    
    # Initialize the random number generator
    rng = np.random.default_rng(rng_seed)
    
    # Sample data
    country_samples = rng.choice(countries, size=num_samples)
    age_samples = rng.choice(ages, size=num_samples)
    gender_samples = rng.choice(genders, size=num_samples)
    
    # Encode gender using LabelEncoder
    label_encoder = LabelEncoder()
    gender_encoded = label_encoder.fit_transform(gender_samples)
    
    # Create DataFrame
    demographics = pd.DataFrame({
        'Country': country_samples,
        'Age': age_samples,
        'Gender': gender_encoded
    })
    
    return demographics