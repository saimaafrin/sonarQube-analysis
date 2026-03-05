import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(rows):
    # Generate random integer values between 0 and 9 for a given number of rows
    data = np.random.randint(0, 10, size=(rows, len(COLUMNS)))
    # Create a Pandas DataFrame with the random integer values
    df = pd.DataFrame(data, columns=COLUMNS)
    # Count the non-zero values in each column
    non_zero_counts = df.count(axis=0)
    # Visualize the information using a bar plot
    fig, ax = plt.subplots()
    ax.bar(non_zero_counts.index, non_zero_counts.values)
    ax.set_xlabel('Column')
    ax.set_ylabel('Number of non-zero values')
    ax.set_title('Number of non-zero values in each column')
    return (df, ax)