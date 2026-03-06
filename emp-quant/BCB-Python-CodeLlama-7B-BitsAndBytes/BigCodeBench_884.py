
import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    # Check if the number of specified columns is 3
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3")

    # Check if the specified columns are contained in df
    if not all(col in df.columns for col in columns):
        raise ValueError("The specified columns are not contained in df")

    # Filter the rows based on the criteria
    filtered_df = df[df['B'] > larger & df['C'] == equal]

    # Compute the contingency table
    contingency_table = pd.crosstab(filtered_df['A'], filtered_df['B'])

    # Perform the chi-square independence test
    p_value = chi2_contingency(contingency_table)[1]

    return p_value

print(task_func(df, ['A', 'B', 'C'], larger=2, equal=50))