
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df = df.fillna(df.mean())
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    
    # Calculate the correlation matrix
    corr_matrix = df_scaled.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df_scaled, plt