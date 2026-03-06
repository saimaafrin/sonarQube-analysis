
import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    if len(columns) != 3:
        raise ValueError("If the number of specified columns is not 3.")
    
    if not all(col in df.columns for col in columns):
        raise ValueError("If the specified columns are not contained in df.")
    
    filtered_df = df[(df[columns[1]] > larger) & (df[columns[2]] == equal)]
    
    if filtered_df.empty:
        raise ValueError("Insufficient data for the test (no rows meeting the criteria).")
    
    contingency_table = pd.crosstab(filtered_df[columns[0]], filtered_df[columns[1]])
    
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    
    return p_value