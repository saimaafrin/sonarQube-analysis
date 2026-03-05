
import seaborn as sns
from random import sample
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    # Remove rows based on values in multiple columns
    for col in tuples:
        df = df[df[col] != tuples[col]]
    # Create random pairs of columns
    pairs = sample(COLUMNS, 2)
    # Generate pairplots
    ax = sns.pairplot(df, x_vars=pairs[0], y_vars=pairs[1])
    return (df, ax)