
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr().round(2)
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    
    # Set the title of the heatmap
    heatmap.set_title(title)
    
    # Return the correlation DataFrame and the Axes object
    return correlation_matrix, heatmap