
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are any numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns found in the DataFrame.")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_df = pd.DataFrame(scaler.fit_transform(numeric_df), columns=numeric_df.columns)
    
    # Create a correlation matrix
    corr_matrix = standardized_df.corr()
    
    # Plot the heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    
    return standardized_df, fig