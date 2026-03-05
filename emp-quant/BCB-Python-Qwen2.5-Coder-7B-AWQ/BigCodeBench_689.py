import numpy as np
from scipy import stats
import pandas as pd
def task_func(df):
    """
    Test if the data in each column of a DataFrame is normally distributed using the Shapiro-Wilk test.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with numeric values.
    
    Returns:
    dict: A dictionary with p-values from the Shapiro-Wilk test for each column.
    """
    p_values = {}
    for column in df.columns:
        p_value = stats.shapiro(df[column])[1]
        p_values[column] = p_value
    return p_values
sample_data = {
    'A': np.random.normal(0, 1, 100),
    'B': np.random.normal(5, 2, 100),
    'C': np.random.exponential(1, 100)
}
df = pd.DataFrame(sample_data)