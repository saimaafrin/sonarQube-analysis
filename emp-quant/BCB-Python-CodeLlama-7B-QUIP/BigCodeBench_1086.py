
import string
import random
import pandas as pd
import numpy as np
# Constants
NUM_SAMPLES = 1000  # Number of samples
def task_func():
    # Generate a list of random strings
    string_list = [random_string(10) for i in range(NUM_SAMPLES)]
    # Generate a list of random floats
    float_list = [random_float(10000) for i in range(NUM_SAMPLES)]
    # Create a DataFrame
    df = pd.DataFrame({'String Field': string_list, 'Float Field': float_list})
    return df

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def random_float(max_value):
    return round(random.uniform(0, max_value), 2)

# Call the function
df = task_func()