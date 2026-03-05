
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    # If there are no numeric columns, raise an error
    if not numeric_cols:
        raise ValueError("No numeric columns in the DataFrame")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Calculate the correlation matrix
    corr_matrix = df[numeric_cols].corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    # Return the standardized DataFrame
    return df