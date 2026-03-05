import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df, plot=False):
    """
    Processes a pandas DataFrame by splitting lists in the 'Value' column into separate columns,
    calculates the Pearson correlation coefficient between these columns, and optionally visualizes
    the correlation matrix using a heatmap.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with columns 'Date' and 'Value'.
    - plot (bool): If True, a heatmap of the correlation matrix is plotted.

    Returns:
    - pd.DataFrame: DataFrame containing the correlation coefficients.
    - Axes: Matplotlib Axes object containing the heatmap plot, returned if 'plot' is True.
    """
    if df.empty:
        raise ValueError("Input DataFrame is empty.")
    
    if 'Value' not in df.columns or not all(isinstance(item, list) for item in df['Value']):
        raise ValueError("Invalid 'Value' column. It should contain lists.")
    
    # Split lists in 'Value' column into separate columns
    df_expanded = pd.DataFrame(df['Value'].tolist(), index=df.index)
    
    # Calculate Pearson correlation coefficient
    correlation_matrix = df_expanded.corr(method='pearson')
    
    if plot:
        # Plotting the correlation matrix as a heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Heatmap')
        plt.show()
    
    return correlation_matrix