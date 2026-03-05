
import seaborn as sns
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the dataframes based on the 'id' column
    merged_df = pd.merge(df1, df2, on="id")

    # Perform a chi-square independence test on the merged dataframe
    contingency_table = merged_df.pivot_table(index=column1, columns=column2, values="id", aggfunc="count")
    p_value = chi2_contingency(contingency_table)[1]

    # Draw a heatmap of the contingency table
    heatmap = sns.heatmap(contingency_table, annot=True, cmap="Blues")

    return p_value, heatmap