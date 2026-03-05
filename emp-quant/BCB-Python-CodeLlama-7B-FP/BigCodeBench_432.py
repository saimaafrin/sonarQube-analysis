import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import chi2_contingency
def task_func(df1, df2, column1="feature1", column2="feature2"):
    """
    Merge two dataframes based on the 'id' column, perform a chi-square independence test on the merged dataframe, and draw a heatmap of the contingency table created from the features in column1, column2.
    The function should output with:
        tuple: A tuple containing:
        p (float): The p-value of the Chi-Squared test.
        heatmap (matplotlib.pyplot.Axes): Seaborn heatmap of the contingency table.
    """
    # Merge the two dataframes based on the 'id' column
    merged_df = pd.merge(df1, df2, on="id")

    # Perform a chi-square independence test on the merged dataframe
    contingency_table = merged_df.groupby([column1, column2]).size().unstack()
    p_value = chi2_contingency(contingency_table)[1]

    # Draw a heatmap of the contingency table
    heatmap = sns.heatmap(contingency_table, annot=True, cmap="Blues")

    return p_value, heatmap
df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": ["a", "a", "b", "b", "c"]})
df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature2": ["x", "y", "z", "x", "y"]})