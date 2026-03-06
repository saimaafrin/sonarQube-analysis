import pandas as pd
import numpy as np
def task_func(d):
    """
    Calculate mean, sum, max, min and standard deviation for the keys "x," "y" and "z" from a list of dictionaries "d."
    
    Parameters:
    d (list): A list of dictionaries.

    Returns:
    dict: A dictionary with keys as 'x', 'y', and 'z' and values as dictionaries of statistics.

    Raises:
    - ValueError: If input is not a list of dictionaries.

    Requirements:
    - pandas
    - numpy

    Examples:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> task_func(data)
    {'x': {'mean': 2.0, 'sum': 6, 'max': 3, 'min': 1, 'std': 0.816496580927726}, 'y': {'mean': 8.666666666666666, 'sum': 26, 'max': 15, 'min': 1, 'std': 5.792715732327589}, 'z': {'mean': 6.0, 'sum': 18, 'max': 7, 'min': 5, 'std': 0.816496580927726}}
    >>> task_func([])
    {'x': None, 'y': None, 'z': None}
    >>> task_func([{'a': 1}])
    {'x': None, 'y': None, 'z': None}
    """
    if not isinstance(d, list):
        raise ValueError("Input must be a list of dictionaries.")
    if not all(isinstance(i, dict) for i in d):
        raise ValueError("Input must be a list of dictionaries.")
    if not all(len(i) == 3 for i in d):
        raise ValueError("Input must be a list of dictionaries with 3 keys.")
    if not all(i.keys() == {'x', 'y', 'z'} for i in d):
        raise ValueError("Input must be a list of dictionaries with 3 keys.")
    if not all(isinstance(i['x'], (int, float)) for i in d):
        raise ValueError("Input must be a list of dictionaries with 3 keys and values of type int or float.")
    if not all(isinstance(i['y'], (int, float)) for i in d):
        raise ValueError("Input must be a list of dictionaries with 3 keys and values of type int or float.")
    if not all(isinstance(i['z'], (int, float)) for i in d):
        raise ValueError("Input must be a list of dictionaries with 3 keys and values of type int or float.")
    df = pd.DataFrame(d)
    df = df.dropna()
    df = df.astype(float)
    df = df.apply(pd.to_numeric)
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')
    df = df.apply(pd.to_numeric, downcast='unsigned')
    df = df.apply(pd.to_numeric, downcast='infer')
    df = df.apply(pd.to_numeric, downcast='float')
    df = df.apply(pd.to_numeric, downcast='integer')
    df = df.apply(pd.to_numeric, downcast='signed')