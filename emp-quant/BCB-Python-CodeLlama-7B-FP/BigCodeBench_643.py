import re
import pandas as pd
import numpy as np
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    The function searches each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    The function should output with:
        pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    """
    # Create a new DataFrame with the same columns as the input DataFrame
    output_df = pd.DataFrame(index=dataframe.index, columns=dataframe.columns)

    # Iterate over each row in the input DataFrame
    for i, row in dataframe.iterrows():
        # Iterate over each column in the input DataFrame
        for j, cell in row.iteritems():
            # Check if the cell value matches the data pattern
            match = re.search(data_pattern, cell)
            if match:
                # Extract the numeric value from the cell
                value = float(match.group(0))
                # Replace the cell value with the extracted value
                output_df.at[i, j] = value
            else:
                # Replace the cell value with NaN
                output_df.at[i, j] = np.nan

    return output_df
dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'],
                          'B': ['>2.34<', '>5.67<', '>8.90<']})