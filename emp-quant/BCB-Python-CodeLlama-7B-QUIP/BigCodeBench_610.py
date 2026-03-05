
from random import sample
import seaborn as sns
import pandas as pd
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows based on values in multiple columns
    for col in COLUMNS:
        df = df.loc[df[col].isnull()]
    # Create n random joint plots of two columns against each other
    plots = []
    if not df.empty:
        for _ in range(n_plots):
            col1, col2 = sample(COLUMNS, 2)
            plots.append(sns.JointGrid(df, col1, col2))
    return df, plots