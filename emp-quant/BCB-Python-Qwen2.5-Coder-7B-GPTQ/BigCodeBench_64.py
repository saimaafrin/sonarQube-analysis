import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Pivot the DataFrame to prepare for the heatmap
    pivot_df = df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='count')
    
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(pivot_df, annot=True, cmap='YlGnBu')
    plt.title('Heatmap of col3 Distribution Grouped by col1 and col2')
    plt.xlabel('col2')
    plt.ylabel('col1')
    
    # Return the DataFrame and the heatmap axes
    return pivot_df, heatmap