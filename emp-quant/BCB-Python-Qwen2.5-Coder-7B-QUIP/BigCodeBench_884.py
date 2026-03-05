
import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    # Check if the number of specified columns is 3
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3.")
    
    # Check if the specified columns are contained in df
    if not all(column in df for column in columns):
        raise ValueError("The specified columns are not contained in df.")
    
    # Filter the DataFrame based on the criteria
    filtered_df = df[(df[columns[1]] > larger) & (df[columns[2]] == equal)]
    
    # Check if there's insufficient data for the test
    if filtered_df.shape[0] == 0:
        raise ValueError("Insufficient data for the test.")
    
    # Create a contingency table from the first two columns of the filtered DataFrame
    contingency_table = pd.crosstab(filtered_df[columns[0]], filtered_df[columns[1]])
    
    # Perform the chi-square independence test
    chi2, p_value, _1, _2 = chi2_contingency(contingency_table)
    
    return p_value

result = task_func(df, ['test', 'hi', 'column3'], larger=2, equal=50)
print(result)  # Output: 0.23810330555354436