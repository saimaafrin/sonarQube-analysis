
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Generate random integer values between 0 and 9 for each column
    data = np.random.randint(0, 10, size=(rows, len(COLUMNS)))
    # Create a Pandas DataFrame with the random data
    df = pd.DataFrame(data, columns=COLUMNS)
    # Count the non-zero values in each column
    counts = df.count(axis=0)
    # Create a bar plot with the counts
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_xlabel('Column')
    ax.set_ylabel('Number of non-zero values')
    ax.set_title('Distribution of non-zero values in each column')
    return (df, ax)