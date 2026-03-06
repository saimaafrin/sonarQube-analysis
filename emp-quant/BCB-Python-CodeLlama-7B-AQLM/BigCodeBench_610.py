from random import sample
import seaborn as sns
import pandas as pd
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    '''
    Remove rows from a dataframe based on values of multiple columns, 
    and then create n random joint plots of two columns against each other if the DataFrame is not empty.
    
    Parameters:
    df (DataFrame): The pandas DataFrame.
    tuples (list): A list of tuples, where each tuple represents a row to be removed.
    n_plots (int): The number of jointplots to be generated.
    
    Returns:
    tuple: A tuple containing:
        - DataFrame: The modified DataFrame.
        - list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    
    Requirements:
    - pandas
    - seaborn
    - random
    
    Example:
    >>> import numpy as np
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    '''
    # Remove rows from the DataFrame
    for tuple in tuples:
        df = df[~(df[COLUMNS].isin(tuple).any(axis=1))]
    
    # Generate joint plots
    plots = []
    if not df.empty:
        for _ in range(n_plots):
            # Select two random columns
            columns = sample(COLUMNS, 2)
            # Generate joint plot
            plot = sns.jointplot(x=columns[0], y=columns[1], data=df)
            # Add plot to list
            plots.append(plot)
    
    return df, plots