
import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    # Generate random strings
    random_strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(NUM_SAMPLES)]
    
    # Generate random floats and format them
    random_floats = [np.random.uniform(0, 10000) for _ in range(NUM_SAMPLES)]
    formatted_floats = [f"{num:,.2f}" for num in random_floats]
    
    # Create DataFrame
    data = {
        'String Field': random_strings,
        'Float Field': formatted_floats
    }
    df = pd.DataFrame(data)
    
    return df