import re
import pandas as pd
import numpy as np
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern. The function searches 
    each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces 
    the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    
    Parameters:
    - dataframe (pd.DataFrame): A pandas DataFrame containing data to be processed.
    - data_pattern (str, optional): data search pattern. Default value is '>\d+\.\d+<'.
    
    Returns:
    - pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    
    Requirements:
    - re
    - pandas
    - numpy
    
    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
    >>> task_func(df)
          A     B
    0  1.23  7.89
    1  4.56  0.12
    """
    # Extract numeric data from each cell
    for col in dataframe.columns:
        for row in dataframe.index:
            cell = dataframe.loc[row, col]
            match = re.search(data_pattern, cell)
            if match:
                dataframe.loc[row, col] = float(match.group(0)[1:-1])
            else:
                dataframe.loc[row, col] = np.nan
    return dataframe