
import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def generate_random_string(length=10):
    """Generate a random string of length `length` using ASCII characters."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_float(min_value=0, max_value=10000, precision=2):
    """Generate a random float between `min_value` and `max_value` with `precision` decimal places."""
    return round(random.uniform(min_value, max_value), precision)

def task_func():
    """Generate a DataFrame with two columns: a string field and a float field."""
    data = []
    for _ in range(NUM_SAMPLES):
        data.append({
            'String Field': generate_random_string(),
            'Float Field': generate_random_float(precision=2)
        })
    return pd.DataFrame(data)