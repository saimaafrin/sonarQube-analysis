import seaborn as sns
import numpy as np
def task_func(df):
    """
    Generates a pair plot from a numeric DataFrame and calculates its covariance matrix.
    The function should raise the exception for:
        ValueError: If the DataFrame is empty.
        TypeError: If the DataFrame contains non-numeric data types.
    The function should output with:
        tuple:
        covariance_df (pandas.DataFrame): The covariance matrix of the input DataFrame.
        pair_plot (sns.axisgrid.PairGrid): Pair plot of the input DataFrame.
    """
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Check if the DataFrame contains non-numeric data types
    if not all(df.dtypes == np.number):
        raise TypeError("The DataFrame contains non-numeric data types.")

    # Calculate the covariance matrix
    covariance_df = df.cov()

    # Generate the pair plot
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})