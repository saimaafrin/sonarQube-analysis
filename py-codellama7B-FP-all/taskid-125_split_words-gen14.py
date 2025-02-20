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

    if ' ' in txt:
        return txt.split(' ')
    if ',' in txt:
        return txt.split(',')
    else:
        i = 0
        result = 0
        for letter in txt:
            if ord(letter.lower()) % 2 == 0:
                result += 1
            i += 1
        return result
