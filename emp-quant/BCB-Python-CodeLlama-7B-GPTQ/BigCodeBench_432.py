import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
def task_func(df1, df2, column1="feature1", column2="feature2"):
    """
    Merge two dataframes based on the 'id' column, perform a chi-square independence test on the merged dataframe, and draw a heatmap of the contingency table created from the features in column1, column2.
    """
    # Merge the two dataframes based on the 'id' column
    merged_df = pd.merge(df1, df2, on="id")

    # Perform a chi-square independence test on the merged dataframe
    contingency_table = merged_df.pivot_table(index=column1, columns=column2, values="id", aggfunc="count")
    p_value = chi2_contingency(contingency_table)[1]

    # Draw a heatmap of the contingency table
    heatmap = sns.heatmap(contingency_table, annot=True, cmap="Blues")

    return p_value, heatmap
df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": ["a", "a", "b", "b", "c"]})
df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature2": ["a", "a", "b", "b", "c"]})