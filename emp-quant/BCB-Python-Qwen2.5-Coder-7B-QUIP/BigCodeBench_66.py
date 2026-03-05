
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in the column 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2']).sum().reset_index()
    
    # Step 3: Create a distribution plot of the 'col3' column using seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='col1', y='col3', hue='col2', data=grouped_df)
    plt.xlabel('col3')
    plt.ylabel('Frequency')
    plt.title('Distribution of col3 by col1 and col2')
    
    # Return the DataFrame and the plot
    return grouped_df, plt