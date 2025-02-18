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

    if test == '':
        return {}
    else:
        test = test.split()
        test_dict = {}
        for i in test:
            if i in test_dict.keys():
                test_dict[i] += 1
            else:
                test_dict[i] = 1
        max_value = max(test_dict.values())
        max_key = [k for k, v in test_dict.items() if v == max_value]
        return {k: v for k, v in test_dict.items() if v == max_value}
