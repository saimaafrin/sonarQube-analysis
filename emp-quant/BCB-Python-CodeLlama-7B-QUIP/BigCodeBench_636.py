
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Generate a random DataFrame with integer values
    data = np.random.randint(0, 9, size=(rows, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    # Count the non-zero values in each column
    non_zero_counts = df.apply(lambda x: x.count())

    # Visualize the results with a bar plot
    fig, ax = plt.subplots()
    ax.bar(non_zero_counts.index, non_zero_counts.values)
    ax.set_xlabel("Column Index")
    ax.set_ylabel("Number of Non-Zero Values")
    ax.set_title("Distribution of Non-Zero Values in Each Column")
    plt.show()

    return (df, ax)