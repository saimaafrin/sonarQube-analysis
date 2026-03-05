
import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    # Generate random strings of 10 ASCII letters
    string_field = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(NUM_SAMPLES)]
    
    # Generate random floats between 0 and 10000 and format them
    float_field = ['{:.2f}'.format(np.random.uniform(0, 10000)) for _ in range(NUM_SAMPLES)]
    
    # Create the DataFrame
    df = pd.DataFrame({
        'String Field': string_field,
        'Float Field': float_field
    })
    
    return df