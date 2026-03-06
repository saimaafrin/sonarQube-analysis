
from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows from the DataFrame based on the values of multiple columns
    for col, val in tuples:
        df = df[df[col] != val]

    # Create n random joint plots of two columns against each other
    if not df.empty:
        joint_plots = []
        for i in range(n_plots):
            col1, col2 = sample(COLUMNS, 2)
            joint_plots.append(sns.JointGrid(data=df, x=col1, y=col2))
            joint_plots[-1].plot_joint(kind='hexbin', color='k')
            joint_plots[-1].plot_marginals(kind='kde', fill=True)
        return df, joint_plots
    else:
        return df, []

df, joint_plots = task_func(df, tuples, n_plots)
print(df)
print(joint_plots)