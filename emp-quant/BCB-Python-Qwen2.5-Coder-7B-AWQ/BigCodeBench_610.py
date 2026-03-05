from random import sample
import seaborn as sns
import pandas as pd
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows based on the values in the specified columns
    df_filtered = df[~df.isin(tuples).all(axis=1)]
    
    # Generate random joint plots if the DataFrame is not empty
    joint_plots = []
    if not df_filtered.empty:
        for _ in range(n_plots):
            # Randomly select two columns for the joint plot
            cols = sample(COLUMNS, 2)
            # Create and append the joint plot to the list
            joint_plot = sns.jointplot(x=cols[0], y=cols[1], data=df_filtered)
            joint_plots.append(joint_plot)
    
    return df_filtered, joint_plots