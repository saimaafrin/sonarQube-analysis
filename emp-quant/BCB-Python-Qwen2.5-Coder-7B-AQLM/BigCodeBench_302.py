
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    if 'Value' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'Value' column.")
    
    if not all(isinstance(val, list) for val in df['Value']):
        raise ValueError("The 'Value' column must contain lists.")
    
    # Split lists in the 'Value' column into separate columns
    df_expanded = pd.DataFrame(df['Value'].tolist()).add_prefix('Value_')
    
    # Calculate the Pearson correlation coefficient
    correlation_matrix = df_expanded.corr(method='pearson')
    
    if plot:
        # Create a heatmap plot
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.show()
    
    return correlation_matrix