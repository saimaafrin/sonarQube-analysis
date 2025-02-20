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


    # if there are no whitespaces
    if txt.find(' ') == -1:
        # check if there are commas
        if txt.find(',') != -1:
            return txt.split(',')
        # if there are no commas, split on whitespaces
        else:
            return txt.split()
    # if there are no commas
    else:
        # return the number of lower-case letters with odd order in the alphabet
        return sum([i for i, j in enumerate(ord(k) - ord('a') % 2) if j == 1])
