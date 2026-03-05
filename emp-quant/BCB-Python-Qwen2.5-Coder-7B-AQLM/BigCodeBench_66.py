
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in the column 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2']).size().reset_index(name='count')
    
    # Step 3: Reset the index of the newly created dataframe
    grouped_df = grouped_df.reset_index()
    
    # Step 4: Create a distribution plot of the 'col3' column using seaborn
    plot = sns.barplot(x='col3', y='count', hue='col1', data=grouped_df)
    plot.set_xlabel('col3')
    
    return grouped_df, plot