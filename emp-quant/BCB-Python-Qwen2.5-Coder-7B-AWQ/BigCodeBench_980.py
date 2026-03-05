import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Plots the correlation matrix from numeric columns in a DataFrame and returns a DataFrame where the numeric columns are standardized to have mean 0 and variance 1.
    
    Parameters:
    df (pandas.DataFrame): Input DataFrame containing numeric and non-numeric columns.
    
    Returns:
    pandas.DataFrame: Standardized DataFrame.
    matplotlib.figure.Figure: Figure object containing the heatmap of the correlation matrix.
    
    Raises:
    ValueError: If the DataFrame is empty or if no numeric columns are present.
    """
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are any numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present in the DataFrame.")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_df = pd.DataFrame(scaler.fit_transform(numeric_df), columns=numeric_df.columns)
    
    # Calculate the correlation matrix
    correlation_matrix = standardized_df.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return standardized_df, plt.gcf()