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


    # If no whitespaces exist in the text we should split on commas.
    if ' ' not in txt:
        # If no commas exist we should return the number of lower-case letters with odd order in the alphabet.
        if ',' not in txt:
            return sum(chr(97 + i) in txt.lower() for i in range(26))
        else:
            return txt.split(',')
    return txt.split()
