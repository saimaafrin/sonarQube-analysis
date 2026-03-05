
from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows based on the conditions in tuples
    for col1, col2, value in tuples:
        df = df[(df[col1] != value) & (df[col2] != value)]

    # Create n random joint plots if the DataFrame is not empty
    plots = []
    if not df.empty:
        for _ in range(n_plots):
            col1, col2 = sample(COLUMNS, 2)
            plots.append(sns.jointplot(x=col1, y=col2, data=df, kind="scatter"))

    return df, plots