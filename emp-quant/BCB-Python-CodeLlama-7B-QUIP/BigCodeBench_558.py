
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Standardize the lists
    scaler = StandardScaler()
    a_std = scaler.fit_transform(a)
    b_std = scaler.transform(b)

    # Create a DataFrame with the standardized values
    df = pd.DataFrame(
        {
            'A': a_std,
            'B': b_std
        },
        columns=columns
    )

    # Visualize the standardized values with a bar plot
    fig, ax = plt.subplots()
    ax.bar(df['A'], df['B'])
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_title('Standardized values')
    plt.show()

    return df, ax