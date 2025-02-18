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

    words = txt.split(',')
    if len(words) > 1:
        return words
    else:
        count = 0
        for i, word in enumerate(txt):
            if word.islower():
                if i % 2 == 0:
                    count += 1
        return count
