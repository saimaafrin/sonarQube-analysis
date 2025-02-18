from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    >>> select_words('Mary had a little lamb', 4)
    ['little']
    >>> select_words('Mary had a little lamb', 3)
    ['Mary', 'lamb']
    >>> select_words('simple white space', 2)
    []
    >>> select_words('Hello world', 4)
    ['world']
    >>> select_words('Uncle sam', 3)
    ['Uncle']
    """

    # TODO: 1. Write a function that satisfies the specification.
    #      2. Test the function.
    #      3. Remove the 'assert' statement.
    #      4. Submit the file.
    assert isinstance(s, str), "The argument s should be a string."
    assert isinstance(n, int), "The argument n should be a natural number."
    assert n >= 0, "The argument n should be a natural number."

    return s.split()
