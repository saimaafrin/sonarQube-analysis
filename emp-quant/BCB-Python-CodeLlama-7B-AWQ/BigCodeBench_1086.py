import string
import random
import pandas as pd
import numpy as np
NUM_SAMPLES = 1000
def task_func():
    """
    Generates a DataFrame with two columns: a string field and a float field.
    The string field contains randomly generated strings of 10 ASCII letters.
    The float field contains randomly generated numbers between 0 and 10000,
    formatted with two decimal places and a comma as the thousands separator.
    """
    # Generate random strings
    string_list = [random.choice(string.ascii_letters) for _ in range(NUM_SAMPLES)]
    # Generate random floats
    float_list = [random.uniform(0, 10000) for _ in range(NUM_SAMPLES)]
    # Format floats
    float_list = [f"{x:.2f}" for x in float_list]
    # Create DataFrame
    df = pd.DataFrame({"String Field": string_list, "Float Field": float_list})
    return df