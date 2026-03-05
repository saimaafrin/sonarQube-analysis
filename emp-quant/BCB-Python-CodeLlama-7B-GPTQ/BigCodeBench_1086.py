import string
import random
import pandas as pd
import numpy as np
NUM_SAMPLES = 1000
def task_func():
    # Generate random strings
    string_list = [random.choice(string.ascii_letters) for _ in range(NUM_SAMPLES)]

    # Generate random floats
    float_list = [random.uniform(0, 10000) for _ in range(NUM_SAMPLES)]

    # Format floats
    float_list = [f"{x:.2f}" for x in float_list]

    # Create DataFrame
    df = pd.DataFrame({
        "String Field": string_list,
        "Float Field": float_list
    })

    return df