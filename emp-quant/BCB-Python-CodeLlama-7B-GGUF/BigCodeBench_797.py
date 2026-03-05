
import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    """
    Count the total number of brackets (i.e., '(', ')', '{', '}', '[', ']') in a pandas DataFrame.

    :param df: The input DataFrame
    :return: The total number of brackets
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    pattern = re.compile(r"[(){}[\]]")
    return sum(pattern.findall(df.to_string()))