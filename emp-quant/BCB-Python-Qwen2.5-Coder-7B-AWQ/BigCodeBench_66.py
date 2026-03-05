import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    """
    Build a pandas DataFrame from a list of elements and create a distribution plot of 'col3' grouped by 'col1' and 'col2'.
    
    Parameters:
    data (list of lists): A list where each element is a list of 3 values.
    
    Returns:
    tuple: A tuple containing a pandas DataFrame and a matplotlib Axes object.
    """
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2']).size().reset_index(name='count')
    
    # Step 3: Create a distribution plot using seaborn
    plot = sns.barplot(x='col3', y='count', hue='col1', data=grouped_df)
    plot.set_xlabel('col3')
    
    return grouped_df, plot