import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Replace NaN values in numeric columns of a dataframe with the average of the column and return a tuple containing:
    - DataFrame: A pandas DataFrame with statistics. This includes count, mean, standard deviation (std), min, 25%, 50%, 75%, and max values for each numeric column.
    - List[Axes]: A list of matplotlib Axes objects representing the distribution plots for each numeric column.
    Each plot visualizes the distribution of data in the respective column with 10 bins.
    """
    # Replace NaN values in numeric columns with the average of the column
    for col in df.select_dtypes(include=['number']).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Calculate statistics for each numeric column
    stats = df.select_dtypes(include=['number']).describe()

    # Create distribution plots for each numeric column
    fig, axs = plt.subplots(nrows=len(df.select_dtypes(include=['number']).columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.select_dtypes(include=['number']).columns):
        sns.distplot(df[col], ax=axs[i], bins=10)

    return (stats, axs)
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, np.nan],
                   'B': [1, 2, 3, 4, 5, np.nan],
                   'C': [1, 2, 3, 4, 5, np.nan]})