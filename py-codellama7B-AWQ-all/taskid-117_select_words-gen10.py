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

    # Solution 1
    return [s for s in s.split() if len([c for c in s if not c.isalpha()]) == n]
    # Solution 2
    return [word for word in s.split() if len([char for char in word if not char.isalpha()]) == n]
    # Solution 3
    return [word for word in s.split() if word.count('^[aeiouAEIOU]') == n]
    # Solution 4
    return [word for word in s.split() if word.count('[^aeiou]') == n]
    # Solution 5
    return [word for word in s.split() if sum([1 for char in word if char.isalpha() and not char.islower()]) == n]
