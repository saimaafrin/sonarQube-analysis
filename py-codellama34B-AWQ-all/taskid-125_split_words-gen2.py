from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    >>> split_words('Hello world!')
    ['Hello', 'world!']
    >>> split_words('Hello,world!')
    ['Hello', 'world!']
    >>> split_words('abcdef')
    3
    """

    words = []
    for letter in txt.split():
        words.append(letter)
    if len(words) == 0:
        words = txt.split(",")
        if len(words) == 0:
            letters = []
            for letter in txt:
                letters.append(letter)
            odd_letters = []
            for letter in letters:
                if letters.index(letter) % 2 == 0:
                    odd_letters.append(letter)
            return len(odd_letters)
        return words
    return words
