import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by col1 and col2
    grouped_df = df.groupby(['col1', 'col2'])

    # Create a heatmap visualization of the distribution of col3 values
    heatmap = sns.heatmap(grouped_df['col3'], annot=True, cmap='Blues')

    # Return the DataFrame and the heatmap visualization
    return df, heatmap
data = [
    ['a', 'b', 1],
    ['a', 'c', 2],
    ['b', 'b', 3],
    ['b', 'c', 4],
    ['c', 'b', 5],
    ['c', 'c', 6]
]