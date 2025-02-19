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


    # your code goes here
    words = []
    for word in s.split():
        vowels = ['a', 'e', 'i', 'o', 'u']
        num_vowels = 0
        for letter in word:
            if letter.lower() in vowels:
                num_vowels += 1
        if num_vowels == n:
            words.append(word)
    return words
