import numpy as np
from scipy import stats
def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values, test if the data in each column is normally distributed using the Shapiro-Wilk test.
    The function should output with:
        dict: A dictionary with p-values from the Shapiro-Wilk test for each column.
    """
    # Initialize an empty dictionary to store the p-values
    p_values = {}

    # Iterate over each column in the DataFrame
    for col in df.columns:
        # Perform the Shapiro-Wilk test on the column
        p_value = stats.shapiro(df[col])[0]

        # Add the p-value to the dictionary
        p_values[col] = p_value

    # Return the dictionary of p-values
    return p_values
df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))