import string
import random
import pandas as pd
import numpy as np
NUM_SAMPLES = 1000
def task_func():
    # Generate random strings
    random_strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(NUM_SAMPLES)]
    
    # Generate random floats and format them
    formatted_floats = [f"{np.random.uniform(0, 10000):,.2f}" for _ in range(NUM_SAMPLES)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'String Field': random_strings,
        'Float Field': formatted_floats
    })
    
    return df