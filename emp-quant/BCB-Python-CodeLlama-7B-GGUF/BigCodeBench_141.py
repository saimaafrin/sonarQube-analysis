
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if rows <= 0:
        raise ValueError("'rows' must be a positive integer greater than 0")

    np.random.seed(seed)
    data = np.random.randint(1, 101, size=(rows, len(columns)))
    df = pd.DataFrame(data, columns=columns)

    means = df.mean(axis=0)
    medians = df.median(axis=0)

    result = {column: {'mean': mean, 'median': median} for column, mean, median in zip(columns, means, medians)}

    return df, result