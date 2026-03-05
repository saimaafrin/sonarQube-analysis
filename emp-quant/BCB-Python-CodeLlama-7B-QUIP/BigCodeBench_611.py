
from random import sample
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    # Remove rows based on values in multiple columns
    for col in tuples:
        df = df[df[col] != tuples[col]]
    # Create n random line plots of two columns against each other
    plots = []
    for i in range(n_plots):
        col1, col2 = sample(COLUMNS, 2)
        plt.plot(df[col1], df[col2])
        plt.show()
    return df, plots