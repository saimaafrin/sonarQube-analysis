import re
import pandas as pd
import numpy as np
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    The function searches each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    """
    # Create a new DataFrame with the same columns as the input DataFrame
    output_df = pd.DataFrame(dataframe.columns, index=dataframe.index)

    # Iterate over each cell in the DataFrame
    for row in dataframe.itertuples():
        for col in dataframe.columns:
            # Check if the cell value matches the pattern
            match = re.search(data_pattern, row[col])
            if match:
                # Extract the numeric value from the match
                value = float(match.group(0))
                # Replace the cell value with the extracted value
                output_df.at[row.Index, col] = value
            else:
                # Replace the cell value with NaN
                output_df.at[row.Index, col] = np.nan

    return output_df
dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'],
                          'B': ['>2.34<', '>5.67<', '>8.90<'],
                          'C': ['>3.45<', '>6.78<', '>9.01<']})