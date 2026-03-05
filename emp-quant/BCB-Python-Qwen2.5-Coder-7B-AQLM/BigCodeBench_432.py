
import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Create a contingency table from the specified columns
    contingency_table = pd.crosstab(merged_df[column1], merged_df[column2])
    
    # Perform the Chi-Squared independence test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Draw a heatmap of the contingency table
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Contingency Table Heatmap')
    plt.xlabel(column1)
    plt.ylabel(column2)
    
    # Return the p-value and the heatmap
    return p, heatmap