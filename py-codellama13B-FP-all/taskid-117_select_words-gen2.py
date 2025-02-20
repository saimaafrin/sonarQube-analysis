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

    # check if the input string contains only letters and spaces
    if not s.isalpha() and not s.isspace():
        raise ValueError('the input string must contain only letters and spaces.')
    
    # check if the input number is positive
    if n < 0:
        raise ValueError('the input number must be positive.')

    # if the input string is empty
    if not s:
        return []

    words = s.split()

    # if the input number is zero
    if n == 0:
        return words

    # if the input number is 1
    if n == 1:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 1]

    # if the input number is 2
    if n == 2:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 2]

    # if the input number is 3
    if n == 3:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 3]

    # if the input number is 4
    if n == 4:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 4]

    # if the input number is 5
    if n == 5:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 5]

    # if the input number is 6
    if n == 6:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 6]

    # if the input number is 7
    if n == 7:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 7]

    # if the input number is 8
    if n == 8:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 8]

    # if the input number is 9
    if n == 9:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 9]

    # if the input number is 10
    if n == 10:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 10]

    # if the input number is 11
    if n == 11:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 11]

    # if the input number is 12
    if n == 12:
        return [w for w in words if len([l for l in w if l.isalpha() and l.islower()]) == 12]

    # if the input number is 13
    if n ==
