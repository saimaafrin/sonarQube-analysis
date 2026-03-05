
import seaborn as sns
from random import sample
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    # Remove rows based on values in specified columns
    for col, val in tuples:
        df = df[df[col] != val]
    # Create n random pairs of columns
    pairs = sample(list(combinations(COLUMNS, 2)), n_plots)
    # Generate pairplots
    axs = []
    for pair in pairs:
        ax = sns.pairplot(df, x_vars=pair[0], y_vars=pair[1])
        axs.append(ax)
    return df, axs