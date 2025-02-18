from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    >>> check_dict_case({ 'a': 'apple', 'b': 'banana' })
    True
    >>> check_dict_case({ 'a': 'apple', 'A': 'banana', 'B': 'banana' })
    False
    >>> check_dict_case({ 'a': 'apple', 8: 'banana', 'a': 'apple' })
    False
    >>> check_dict_case({ 'Name': 'John', 'Age': '36', 'City': 'Houston' })
    False
    >>> check_dict_case({ 'STATE': 'NC', 'ZIP': '12345' })
    True
    """

    if len(dict) == 0:
        return False
    else:
        keys = list(dict.keys())
        if len(keys) == 1:
            return True
        else:
            i = 0
            while i < len(keys) - 1:
                if keys[i].islower() and keys[i + 1].isupper():
                    return False
                if keys[i].isupper() and keys[i + 1].islower():
                    return False
                i += 1
            return True
