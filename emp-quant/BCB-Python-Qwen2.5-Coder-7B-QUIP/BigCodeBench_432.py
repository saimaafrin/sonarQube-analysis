
import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the two dataframes on the 'id' column
    merged_df = df1.merge(df2, on='id')
    
    # Create a contingency table from the features in column1 and column2
    contingency_table = pd.crosstab(merged_df[column1], merged_df[column2])
    
    # Perform a chi-square independence test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Draw a heatmap of the contingency table
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.title('Contingency Table Heatmap')
    plt.show()
    
    return p, heatmap