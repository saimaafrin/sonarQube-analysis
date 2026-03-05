import re
import pandas as pd
def task_func(df: pd.DataFrame) -> int:
    """
    Count the total number of brackets (i.e., '(', ')', '{', '}', '[', ']') in a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    pattern = re.compile(r"[(){}[\]]")
    return sum(pattern.findall(df.to_string()))
df = pd.DataFrame({'Test': ['(a)', 'b', '[[[[))c']})