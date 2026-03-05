import re
import pandas as pd
def task_func(df: pd.DataFrame) -> int:
    """
    Count the total number of brackets (i.e., '(', ')', '{', '}', '[', ']') in a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    pattern = re.compile(r"[(){}[\]]")
    total_brackets = 0

    for col in df.columns:
        for cell in df[col]:
            total_brackets += len(re.findall(pattern, cell))

    return total_brackets
df = pd.DataFrame({'Test': ['(a)', 'b', '[[[[))c']})