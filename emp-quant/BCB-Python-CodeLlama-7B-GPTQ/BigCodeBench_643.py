import re
import pandas as pd
import numpy as np
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    The function searches each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    """
    # Create a new DataFrame with the extracted numeric values
    new_dataframe = pd.DataFrame(index=dataframe.index, columns=dataframe.columns)

    # Iterate over each cell in the DataFrame
    for row in dataframe.itertuples():
        for col in dataframe.columns:
            # Extract the numeric value from the cell content
            match = re.search(data_pattern, getattr(row, col))
            if match:
                # Replace the cell content with the extracted numeric value
                new_dataframe.at[row.Index, col] = float(match.group(0))
            else:
                # Replace the cell content with NaN if no match is found
                new_dataframe.at[row.Index, col] = np.nan

    return new_dataframe
dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'],
                          'B': ['>10.11<', '>20.22<', '>30.33<'],
                          'C': ['>40.44<', '>50.55<', '>60.66<']})