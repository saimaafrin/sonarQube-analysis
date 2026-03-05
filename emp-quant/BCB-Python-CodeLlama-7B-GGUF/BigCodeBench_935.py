
import pandas as pd
import string

def task_func(word):
    """
    Creates a Pandas DataFrame from a single word, where each row contains a letter from the word and its 1-based position in the alphabet.

    Parameters
    ----------
    word : str
        The input word.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with two columns: 'Letter' and 'Position', where 'Position' is the letter's position in the English alphabet.

    Raises
    ------
    ValueError
        If the input word is not in lowercase or contains non-alphabetic characters.
    """
    if not word.islower():
        raise ValueError("Input word must be in lowercase.")
    if not all(c in string.ascii_letters for c in word):
        raise ValueError("Input word must contain only alphabetic characters.")

    df = pd.DataFrame(columns=["Letter", "Position"])
    for i, c in enumerate(word, start=1):
        df = df.append({"Letter": c, "Position": i}, ignore_index=True)
    return df