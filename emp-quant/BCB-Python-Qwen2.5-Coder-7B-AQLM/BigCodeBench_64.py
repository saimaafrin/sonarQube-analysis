
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Pivot the DataFrame to prepare for the heatmap
    pivot_df = df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='count')
    
    # Create the heatmap
    heatmap = sns.heatmap(pivot_df, annot=True, cmap='YlGnBu')
    
    # Set the title and labels
    heatmap.set_title('Distribution of col3 by col1 and col2')
    heatmap.set_xlabel('col2')
    heatmap.set_ylabel('col1')
    
    # Return the DataFrame and the heatmap
    return df, heatmap