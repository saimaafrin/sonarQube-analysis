
import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    """
    Count the total number of brackets in a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to count the brackets in.

    Returns
    -------
    int
        The total number of brackets.

    Raises
    ------
    TypeError
        If input is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    pattern = re.compile(r"[(){}[\]]")
    bracket_count = 0

    for col in df.columns:
        for cell in df[col]:
            bracket_count += len(pattern.findall(cell))

    return bracket_count