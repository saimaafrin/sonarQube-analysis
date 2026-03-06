
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Pivot table to prepare data for heatmap
    pivot_table = df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='count')
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Heatmap of col3 Distribution Grouped by col1 and col2')
    plt.xlabel('col2')
    plt.ylabel('col1')
    
    return df, heatmap