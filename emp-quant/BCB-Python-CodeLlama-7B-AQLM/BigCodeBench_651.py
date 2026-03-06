import pandas as pd
import time
def task_func(df, target_value):
    '''
    Convert the input dic of list to DataFrame and searcher in this DataFrame for rows with cells equal to the
    provided target_value. It then plots the count of such rows per column.

    Parameters:
    - df (dic of list): The input dict. It should have a 'Name' key.
    - target_value (str): The target value to be searched in the DataFrame.

    Returns:
    tuple: A tuple containing:
        - A pandas Series with counts of the target value per column.
        - A matplotlib Axes object representing the plot (None if dataframe is empty).

    Requirements:
    - pandas
    - time

    Example:
    >>> df = {'Column1': ['0', 'a', '332', '33']}
    >>> series, ax = task_func(df, '332')
    '''
    df = pd.DataFrame(df)
    if df.empty:
        return pd.Series(), None
    df = df.applymap(str)
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('-', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('_', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('.', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(',', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(';', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(':', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('(', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(')', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('[', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace(']', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('{', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('}', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace("'", '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('`', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('~', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('!', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('@', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('#', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('$', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('%', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('^', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('&', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('*', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('=', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('+', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('<', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('>', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('?', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('/', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('\\', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('|', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)