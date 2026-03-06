
import re
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    The function searches each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    """
    # Create a new DataFrame with the same columns as the input DataFrame
    new_dataframe = pd.DataFrame(index=dataframe.index, columns=dataframe.columns)

    # Iterate over each row and column in the DataFrame
    for i, row in dataframe.iterrows():
        for j, cell in row.iteritems():
            # Check if the cell value matches the data pattern
            match = re.search(data_pattern, cell)
            if match:
                # Extract the numeric value from the match
                value = float(match.group(0)[1:-1])
                # Replace the cell value with the extracted value
                new_dataframe.at[i, j] = value
            else:
                # Replace the cell value with NaN
                new_dataframe.at[i, j] = np.nan

    return new_dataframe