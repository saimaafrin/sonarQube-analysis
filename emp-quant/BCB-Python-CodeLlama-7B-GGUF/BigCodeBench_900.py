
import pandas as pd
import numpy as np

def task_func(d):
    if not isinstance(d, list) or not all(isinstance(x, dict) for x in d):
        raise ValueError("Input must be a list of dictionaries")

    df = pd.DataFrame(d)
    stats = df.describe()
    stats = {k: v for k, v in stats.items() if k in ["x", "y", "z"]}
    return stats