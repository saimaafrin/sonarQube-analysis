import numpy as np
import pandas as pd
def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    """
    Create a Pandas DataFrame with a specified number of rows filled with random values in [0, 1) and shuffled columns.
    Note that:
        - The columns should be unique and sorted in the ascending order.
        - The function should output with:
            - pd.DataFrame: A pandas DataFrame with shuffled columns.
    """
    np.random.seed(seed)
    data = np.random.rand(rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    df = df.sort_values(by=columns, ascending=True)
    return df
rows = 10
columns = ["A", "B", "C", "D", "E"]