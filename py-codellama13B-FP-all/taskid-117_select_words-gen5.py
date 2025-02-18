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

    # Replace the words with only their first letter
    temp = s.lower()
    for i in range(len(temp)):
        if temp[i] != ' ':
            temp = temp.replace(temp[i], temp[i].lower(), 1)
    words = temp.split()
    # Create a list of all words that contain n consonants
    final = []
    for word in words:
        if word.count('b') + word.count('c') + word.count('d') + word.count('f') + word.count('g') + \
            word.count('h') + word.count('j') + word.count('k') + word.count('l') + word.count('m') + \
            word.count('n') + word.count('p') + word.count('q') + word.count('r') + word.count('s') + \
            word.count('t') + word.count('v') + word.count('w') + word.count('x') + word.count('y') + \
            word.count('z') == n:
            final.append(word)
    return final
