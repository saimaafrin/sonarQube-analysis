
import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    if len(df) < 5:
        raise ValueError("Insufficient data for the test")
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3")
    for col in columns:
        if col not in df.columns:
            raise ValueError("The specified columns must be contained in df")
    filtered_df = df[(df[columns[1]] > larger) & (df[columns[2]] == equal)]
    contingency_table = pd.crosstab(filtered_df[columns[0]], filtered_df[columns[1]])
    _, p_value, _, _ = chi2_contingency(contingency_table)
    return p_value