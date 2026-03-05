
from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on values of multiple columns,
    and then create n random joint plots of two columns against each other
    if the DataFrame is not empty.

    Args:
        df (pd.DataFrame): The input DataFrame.
        tuples (list): A list of tuples containing column names and values.
        n_plots (int): The number of joint plots to generate.

    Returns:
        tuple: A tuple containing:
            DataFrame: The modified DataFrame.
            list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty,
                   otherwise an empty list.
    """
    # Remove rows based on values of multiple columns
    for col_name, value in tuples:
        df = df[df[col_name] == value]

    # Check if the DataFrame is empty
    if df.empty:
        return df, []

    # Generate n random joint plots
    joint_plots = []
    for _ in range(n_plots):
        # Select two random columns
        col1, col2 = sample(COLUMNS, 2)
        # Generate a joint plot
        joint_plot = sns.jointplot(x=col1, y=col2, data=df)
        joint_plots.append(joint_plot)

    return df, joint_plots

# Remove rows based on values of multiple columns
tuples = [('A', 3), ('B', 30), ('C', 300)]

# Generate 2 random joint plots
n_plots = 2

# Call the function
df, joint_plots = task_func(df, tuples, n_plots)

# Print the modified DataFrame
print(df)

# Print the generated joint plots
for joint_plot in joint_plots:
    print(joint_plot)