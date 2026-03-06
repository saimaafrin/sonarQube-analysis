
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if rows <= 0:
        raise ValueError("'rows' must be a positive integer greater than 0")

    np.random.seed(seed)
    data = np.random.randint(1, 100, size=(rows, len(columns)))
    df = pd.DataFrame(data, columns=columns)

    means = {}
    medians = {}
    for col in columns:
        means[col] = df[col].mean()
        medians[col] = statistics.median(df[col])

    return df, means, medians