
import seaborn as sns
from random import sample
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    # Remove rows from the DataFrame based on the specified tuples
    for col1, col2 in tuples:
        df = df[df[col1] != df[col2]]

    # Create n random pairs of columns to generate pairplots
    pairs = sample(COLUMNS, n_plots)

    # Generate pairplots for each pair
    axs = []
    for pair in pairs:
        ax = sns.pairplot(df, x_vars=pair, y_vars=pair)
        axs.append(ax)

    return df, axs

# Remove rows where A and B are equal
tuples = [('A', 'B')]
n_plots = 2

# Call the function
df, axs = task_func(df, tuples, n_plots)

# Print the modified DataFrame
print(df)

# Print the generated pairplots
for ax in axs:
    print(ax)