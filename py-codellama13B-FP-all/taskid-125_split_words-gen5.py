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


    txt = txt.strip()
    if len(txt) == 0:
        return 0
    if ' ' in txt:
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    else:
        return len([i for i in range(ord('a'), ord('z') + 1, 2) if txt[i % len(txt)].islower()])
