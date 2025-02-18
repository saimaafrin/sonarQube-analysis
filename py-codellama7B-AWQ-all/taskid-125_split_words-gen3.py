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

    # Your code here
    words = []
    for char in txt:
        if char in ' ' or char == ',':
            words.append(txt[:words.index(char)])
            txt = txt[words.index(char)+1:]

    if not words:
        count = 0
        for i in range(26):
            if ord('a')+i < ord('z')+i:
                count += 1
        return count
    else:
        return words
