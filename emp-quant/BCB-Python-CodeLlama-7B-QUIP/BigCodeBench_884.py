
import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    # Check if the number of specified columns is 3
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3")

    # Check if the specified columns are contained in df
    for column in columns:
        if column not in df:
            raise ValueError(f"{column} is not contained in the DataFrame")

    # Filter the DataFrame based on the specified criteria
    df = df.loc[df['A'] > larger and df['B'] == equal]

    # Compute the contingency table of the first two columns
    contingency_table = pd.crosstab(df['A'], df['B'])

    # Perform the chi-square independence test
    result = chi2_contingency(contingency_table, correction=False)

    # Return the p-value
    return result.pvalue