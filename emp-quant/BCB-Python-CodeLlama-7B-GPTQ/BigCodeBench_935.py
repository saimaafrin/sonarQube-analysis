import pandas as pd
import string
def task_func(word):
    """
    Creates a Pandas DataFrame from a single word, where each row contains a letter from the word and its 1-based position in the alphabet.
    """
    # Check if the input word is in lowercase and contains only alphabetic characters
    if not word.islower() or any(char not in string.ascii_lowercase for char in word):
        raise ValueError("Input word must be in lowercase and contain only alphabetic characters")

    # Create a list of tuples with the letter and its position in the alphabet
    letters = [(letter, string.ascii_lowercase.index(letter) + 1) for letter in word]

    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame(letters, columns=["Letter", "Position"])

    return df