
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2'])['col3'].value_counts().reset_index(name='count')
    
    # Step 3: Create a distribution plot using seaborn
    plot = sns.barplot(x='col3', y='count', hue='col1', data=grouped_df)
    plot.set_xlabel('col3')
    
    # Return the DataFrame and the plot object
    return grouped_df, plot