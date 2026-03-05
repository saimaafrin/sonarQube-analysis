import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
def task_func(data, col1, col2):
    """
    Perform a chi-square test of independence of variables in a contingency table.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing categorical data.
    col1 : str
        Name of the first column.
    col2 : str
        Name of the second column.

    Returns
    -------
    float
        The p-value of the chi-square test of independence.

    Raises
    ------
    ValueError
        If 'data' is empty, if 'col1' or 'col2' are not in 'data', if one or both of the columns do not have multiple categories, or if some categories have less than 5 observations (violating the chi-square test assumptions).
    TypeError
        If one or both of the columns contain non-categorical data.
    """
    # Check if data is empty
    if data.empty:
        raise ValueError("Data is empty.")

    # Check if col1 and col2 are in data
    if col1 not in data.columns or col2 not in data.columns:
        raise ValueError("Columns not in data.")

    # Check if col1 and col2 have multiple categories
    if data[col1].nunique() < 2 or data[col2].nunique() < 2:
        raise ValueError("Not enough categories in columns.")

    # Check if some categories have less than 5 observations (violating the chi-square test assumptions)
    if data[col1].value_counts().min() < 5 or data[col2].value_counts().min() < 5:
        raise ValueError("Not enough observations in categories.")

    # Check if columns contain non-categorical data
    if not data[col1].dtypes.kind == "O" or not data[col2].dtypes.kind == "O":
        raise TypeError("Columns contain non-categorical data.")

    # Construct contingency table
    contingency_table = pd.crosstab(data[col1], data[col2])

    # Perform chi-square test of independence
    p_value = chi2_contingency(contingency_table)[1]

    return p_value
data = pd.DataFrame({
    'a': np.random.choice(['A', 'B'], size=100),
    'b': np.random.choice(['X', 'Y'], size=100)
})