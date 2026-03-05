
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    last_column = df.iloc[:, -1]
    plt.figure()
    ax = last_column.plot(kind='hist', bins=bins, edgecolor='k')
    ax.set_title(f'Histogram of {last_column.name}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.show()
    return ax