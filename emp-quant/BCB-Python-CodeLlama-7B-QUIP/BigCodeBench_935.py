
import pandas as pd
import string
def task_func(word):
    if not all(c in string.ascii_lowercase for c in word):
        raise ValueError("Input word must be in lowercase and contain only alphabetic characters")
    df = pd.DataFrame({'Letter': list(word), 'Position': [ord(c) - ord('a') + 1 for c in word]})
    return df