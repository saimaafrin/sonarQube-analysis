import pandas as pd
from scipy.stats import chi2_contingency
def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    """
    Filters a pandas DataFrame based on the values of specific rows, and performs a chi-square independence test on the first two columns.
    The function filters rows based on the following criteria:
    Keep only rows where:
        The value of the second column: df['second'] > larger
        The value of the third column: df['third'] == equal
    After filtering a contingency table of the first two columns is computed, which is then used in the chi2 independence test.
    The p-value of the test is returned.
    """
    if len(df) < 5:
        raise ValueError("Insufficient data for the test")
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3")
    if not all(col in df.columns for col in columns):
        raise ValueError("The specified columns must be contained in df")

    # Filter the data
    filtered_df = df[df[columns[1]] > larger]
    filtered_df = filtered_df[filtered_df[columns[2]] == equal]

    # Compute the contingency table
    contingency_table = pd.crosstab(filtered_df[columns[0]], filtered_df[columns[1]])

    # Perform the chi-square independence test
    p_value = chi2_contingency(contingency_table)[1]

    return p_value
df = pd.DataFrame({
    'test': ['A', 'b', 'b', 'a', 'c', 'd'],
    'hi': [45, 2, 2, 3, 4, 4],
    'column3': [50, 50, 50, 50, 50, 50]
})