
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a DataFrame from the list of lists
    df = pd.DataFrame(data, columns=COLUMNS)
    # Group the DataFrame by "col1" and "col2"
    grouped_df = df.groupby(['col1', 'col2'])
    # Aggregate the grouped DataFrame to get the distribution of "col3"
    agg_df = grouped_df.agg({'col3': 'count'})
    # Visualize the heatmap
    ax = sns.heatmap(agg_df, annot=True, cmap='viridis')
    plt.show()
    return (df, ax)