
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")
    if not (items and locations):
        items = ['Item1', 'Item2', 'Item3']
        locations = ['Location1', 'Location2', 'Location3']
    counts = df.groupby(['Item', 'Location']).count()
    counts = counts.reset_index()
    counts.columns = ['Item', 'Location', 'Count']
    counts = counts[['Item', 'Location', 'Count']]
    ax = counts.plot.bar(x='Item', y='Count', figsize=(10, 10), title='Distribution of Items by Location')
    plt.show()
    return ax