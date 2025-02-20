from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """

    letter_dict = {}
    if not test:
        return letter_dict

    for letter in test.split():
        if letter_dict.get(letter):
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    for letter, count in list(letter_dict.items()):
        if len(letter_dict.keys()) > 1:
            if count != max(letter_dict.values()):
                letter_dict.pop(letter)
        else:
            letter_dict.pop(letter)
    
    return letter_dict
