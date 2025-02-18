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

    # Implement your function here, take care to use the variable names provided in the docstring
    if txt.find(' ') != -1:
        return txt.split()
    elif txt.find(',') != -1:
        return txt.split(',')
    else:
        return sum([1 for i in txt if ord(i) % 2 == 0])
