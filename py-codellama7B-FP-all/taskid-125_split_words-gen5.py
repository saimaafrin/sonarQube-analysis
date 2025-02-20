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

    words = txt.split()
    if len(words) > 0:
        return words
    else:
        words = txt.split(',')
        if len(words) > 0:
            return words
        else:
            word = [ord(char) for char in txt]
            for i, char in enumerate(word):
                if char % 2 != 0 and char > ord('z') and char > ord('a'):
                    return i
            return len(word)
