
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr().round(2)
    
    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title(title)
    
    return corr_matrix, ax