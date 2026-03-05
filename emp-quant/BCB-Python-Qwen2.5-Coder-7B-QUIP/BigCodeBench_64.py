
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Pivot the DataFrame to prepare for the heatmap
    pivot_df = df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='mean')
    
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(pivot_df, annot=True, cmap='viridis')
    
    # Return the DataFrame and the heatmap axes
    return df, heatmap