import nltk
from string import punctuation
import pandas as pd
def task_func(text):
    """
    Finds all words in a text, that are seperated by whitespace, 
    beginning with the "$" character and computes their number of occurences.

    Parameters:
    text (str): The input text.

    Returns:
    DataFrame: A pandas DataFrame with two columns: "Word" and "Frequency". 
               "Word" contains the '$' prefixed words, and "Frequency" contains their occurrences.

               
    Raises:
    ValueError: if text is not a string
    
    Requirements:
    - nltk
    - string
    - pandas

    Note:
    The function ignores words that are entirely made up of punctuation, even if they start with a '$'.

    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> task_func(text)
       Word  Frequency
    0  $abc          3
    1  $efg          1
    2  $hij          3

    >>> text = "$hello this i$s a $test $test $test"
    >>> task_func(text)
         Word  Frequency
    0  $hello          1
    1   $test          3
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    # remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))

    # split text into words
    words = text.split()

    # filter words that start with $
    words = [word for word in words if word.startswith("$")]

    # count occurences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # create dataframe
    df = pd.DataFrame(word_count.items(), columns=["Word", "Frequency"])

    return df