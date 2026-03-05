import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros, and then output the distribution of each column after replacing.
    """
    # Replace all elements in DataFrame columns that do not exist in the target_values array with zeros
    for col in df.columns:
        df[col] = df[col].replace(to_replace=df[col].unique().difference(target_values), value=0)

    # Output the distribution of each column after replacing
    for col in df.columns:
        sns.distplot(df[col], label=col)

    # Label each plot as the name of the column it corresponds to
    plt.legend()

    return plt.gca()
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5], 'C': [1, 2, 3, 4, 5]})
target_values = [1, 3, 4]