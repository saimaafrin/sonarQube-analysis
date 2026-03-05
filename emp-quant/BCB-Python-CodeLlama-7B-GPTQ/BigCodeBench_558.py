import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(a, b, columns=['A', 'B']):
    # Standardize the data
    scaler = StandardScaler()
    a_std = scaler.fit_transform(a)
    b_std = scaler.fit_transform(b)

    # Create a DataFrame with the standardized values
    df = pd.DataFrame({'A': a_std, 'B': b_std}, columns=columns)

    # Visualize the standardized values using a bar plot
    fig, ax = plt.subplots()
    ax.bar(df['A'], df['B'])
    ax.set_xlabel('Standardized A')
    ax.set_ylabel('Standardized B')
    ax.set_title('Standardized Data')
    plt.show()

    return df, ax
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]