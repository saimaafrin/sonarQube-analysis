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

    # 1. Check if the input string is not empty.
    # 2. Initialize the result list.
    # 3. Initialize the current word.
    # 4. Iterate through the characters in the input string.
    #    a. If the character is a consonant, increment the number of consonants 
    #       in the current word.
    #    b. If the character is a space, add the current word to the result list.
    # 5. Return the result list.
    if len(s) == 0:
        return []
    result: List[str] = []
    word: str = ""
    for c in s:
        if c.isalpha():
            word += c
        else:
            if len(word) == n:
                result.append(word)
            word = ""
    if len(word) == n:
        result.append(word)
    return result
