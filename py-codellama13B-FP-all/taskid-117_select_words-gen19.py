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

    # 296ms 45.16%
    # 18.4MB 62.63%
    word_list = []
    if s == '':
        return []
    else:
        for i in range(len(s.split(' '))):
            if s.split(' ')[i].count('a') + s.split(' ')[i].count('e') + s.split(' ')[i].count('i') + s.split(' ')[i].count('o') + s.split(' ')[i].count('u') == n:
                word_list.append(s.split(' ')[i])
            else:
                continue
    return word_list
