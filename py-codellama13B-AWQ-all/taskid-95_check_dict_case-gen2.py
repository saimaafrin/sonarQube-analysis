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

    if not dict:
        return False
    if len(dict) == 1:
        return True
    first_key = next(iter(dict))
    first_value = dict[first_key]
    if isinstance(first_key, str) and (first_key.islower() or first_key.isupper()):
        for key in dict:
            if (key.islower() and first_key.isupper()) or (key.isupper() and first_key.islower()):
                return False
            if isinstance(key, str) and (key.islower() or key.isupper()):
                if isinstance(dict[key], str):
                    if dict[key].islower() and key.isupper():
                        return False
                    if dict[key].isupper() and key.islower():
                        return False
    return False
