
import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    def reverse_words(words: list) -> list:
        new_words = []
        for word in words:
            if re.match(pattern, word):
                new_words.append(word[::-1])
            else:
                new_words.append(word)
        return new_words
    new_df = df.copy()
    new_df[column_name] = reverse_words(df[column_name].tolist())
    return new_df