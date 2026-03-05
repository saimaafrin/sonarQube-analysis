import string
import random
import pandas as pd
import numpy as np
NUM_SAMPLES = 1000
def task_func():
    # Generate random strings of 10 ASCII letters
    random_strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(NUM_SAMPLES)]
    
    # Generate random floats between 0 and 10000
    random_floats = np.random.uniform(0, 10000, NUM_SAMPLES)
    
    # Format floats with two decimal places and a comma as the thousands separator
    formatted_floats = [f"{num:,.2f}" for num in random_floats]
    
    # Create DataFrame
    df = pd.DataFrame({
        'String Field': random_strings,
        'Float Field': formatted_floats
    })
    
    return df