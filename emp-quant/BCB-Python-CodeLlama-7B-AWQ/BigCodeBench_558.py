import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(a, b, columns=['A', 'B']):
    """
    Standardize two lists of numbers using the StandardScaler from sklearn and visualize the standardized values using a bar plot.
    """
    # Create DataFrames for the two lists
    df_a = pd.DataFrame(a, columns=columns)
    df_b = pd.DataFrame(b, columns=columns)

    # Standardize the data
    scaler = StandardScaler()
    df_a_std = scaler.fit_transform(df_a)
    df_b_std = scaler.fit_transform(df_b)

    # Create a DataFrame for the standardized values
    df_std = pd.concat([df_a_std, df_b_std], axis=1)

    # Visualize the standardized values using a bar plot
    fig, ax = plt.subplots()
    ax.bar(df_std.index, df_std['A'], label='A')
    ax.bar(df_std.index, df_std['B'], label='B')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized value')
    ax.set_title('Standardized values')
    ax.legend()

    return df_std, ax
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]