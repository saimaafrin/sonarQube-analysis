
import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    # Generate random strings
    string_list = [random.choice(string.ascii_letters) for _ in range(NUM_SAMPLES)]

    # Generate random floats
    float_list = [random.uniform(0, 10000) for _ in range(NUM_SAMPLES)]

    # Create DataFrame
    df = pd.DataFrame({'String Field': string_list, 'Float Field': float_list})

    # Format floats with two decimal places and comma as thousands separator
    df['Float Field'] = df['Float Field'].apply(lambda x: "{:,}".format(x))

    return df

# Call the function
df = task_func()

# Print the DataFrame
print(df)