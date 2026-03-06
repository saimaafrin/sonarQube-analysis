
from random import sample
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    # Remove rows from the DataFrame based on values of multiple columns
    for col, val in tuples:
        df = df[df[col] != val]
    # Create n random line plots of two columns against each other
    plot_details = []
    for i in range(n_plots):
        col1, col2 = sample(COLUMNS, 2)
        plot_details.append((col1, col2))
        plt.plot(df[col1], df[col2])
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f'{col1} vs {col2}')
        plt.show()
    return (df, plot_details)