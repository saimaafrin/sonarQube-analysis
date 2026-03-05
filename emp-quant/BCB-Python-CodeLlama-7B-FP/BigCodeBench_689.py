import numpy as np
from scipy import stats
import pandas as pd
import numpy as np
def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values, test if the data in each column is normally distributed using the Shapiro-Wilk test.
    The function should output with:
        dict: A dictionary with p-values from the Shapiro-Wilk test for each column.
    """
    # Perform Shapiro-Wilk test on each column of the DataFrame
    p_values = {}
    for col in df.columns:
        p_values[col] = stats.shapiro(df[col])[0]

    return p_values
df = pd.DataFrame(np.random.randn(100, 5))