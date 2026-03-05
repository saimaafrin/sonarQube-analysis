
import re
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def task_func(dataframe, data_pattern=DATA_PATTERN):
    # Create a new DataFrame with the same columns as the input DataFrame
    output_df = pd.DataFrame(index=dataframe.index, columns=dataframe.columns)

    # Iterate over each cell in the input DataFrame
    for row in dataframe.itertuples():
        # Extract the cell value as a string
        cell_value = str(row[1])

        # Search for the pattern in the cell value
        match = re.search(data_pattern, cell_value)

        # If a match is found, extract the numeric value and replace the cell value
        if match:
            numeric_value = float(match.group(0)[1:-1])
            output_df.loc[row[0], row[1]] = numeric_value
        # If no match is found, replace the cell value with NaN
        else:
            output_df.loc[row[0], row[1]] = np.nan

    return output_df