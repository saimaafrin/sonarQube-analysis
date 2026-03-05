
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if not numeric_cols.size:
        raise ValueError("No numeric columns are present in the DataFrame.")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    df_numeric_scaled = df[numeric_cols].copy()
    df_numeric_scaled[numeric_cols] = scaler.fit_transform(df_numeric_scaled[numeric_cols])
    
    # Create a correlation matrix
    corr_matrix = df_numeric_scaled.corr()
    
    # Plot the correlation matrix as a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df_numeric_scaled, plt.gcf()