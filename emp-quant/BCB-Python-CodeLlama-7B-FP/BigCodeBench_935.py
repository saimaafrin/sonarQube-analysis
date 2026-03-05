import pandas as pd
import string
def task_func(word):
    """
    Creates a Pandas DataFrame from a single word, where each row contains a letter from the word and its 1-based position in the alphabet.
    """
    if not word.islower():
        raise ValueError("Input word must be in lowercase")
    if not all(c in string.ascii_letters for c in word):
        raise ValueError("Input word must contain only alphabetic characters")

    df = pd.DataFrame(columns=["Letter", "Position"])
    for i, c in enumerate(word):
        df = df.append({"Letter": c, "Position": i + 1}, ignore_index=True)
    return df