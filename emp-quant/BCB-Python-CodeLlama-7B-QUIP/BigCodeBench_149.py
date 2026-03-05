
import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    if include_index:
        df = pd.DataFrame(columns=DEFAULT_COLUMNS + ['Index'])
    else:
        df = pd.DataFrame(columns=DEFAULT_COLUMNS)
    for i, element in enumerate(elements):
        df.loc[i] = [element, len(element)]
    return df