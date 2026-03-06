import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
RANGE = 100
SIZE = 1000
def task_func():
    """
    Generates a DataFrame with two columns, 'X' and 'Y', each filled with random integers within a specified range,
    and plots these points using a scatter plot. The visualization is created using Seaborn on top of Matplotlib.

    The function is designed to be parameter-free for simplicity, utilizing constants for configuration.

    Returns:
        pd.DataFrame: A DataFrame with 'X' and 'Y' columns containing the generated random integers.

    Requirements:
        - numpy
        - pandas
        - seaborn
        - matplotlib.pyplot

    No Parameters.

    Example:
        >>> df = task_func()
        >>> isinstance(df, pd.DataFrame)
        True
        >>> 'X' in df.columns and 'Y' in df.columns
        True
        >>> len(df)
        1000
        >>> all(df['X'].between(0, RANGE - 1)) and all(df['Y'].between(0, RANGE - 1))
        True
    """
    # Generate random integers within the specified range
    x = np.random.randint(0, RANGE, SIZE)
    y = np.random.randint(0, RANGE, SIZE)

    # Create a DataFrame with the generated integers
    df = pd.DataFrame({'X': x, 'Y': y})

    # Plot the points using a scatter plot
    sns.scatterplot(x='X', y='Y', data=df)

    # Return the DataFrame
    return df