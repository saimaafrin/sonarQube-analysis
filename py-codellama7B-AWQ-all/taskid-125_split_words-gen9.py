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

    if len(txt) == 0:
        return 0
    if not ' ' in txt:
        if not ',':
            letters = 0
            for i in txt:
                if i.islower():
                    letters += 1
            return letters
    else:
        return [i for i in txt.split(' ')]

    return txt.split(',')
