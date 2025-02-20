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

    # check if the dictionary is empty
    if len(dict) == 0:
        return False
    # check if all keys are strings
    if not all(isinstance(key, str) for key in dict.keys()):
        return False
    # check if all keys are in upper case
    if all(key.isupper() for key in dict.keys()):
        return True
    # check if all keys are in lower case
    elif all(key.islower() for key in dict.keys()):
        return True
    # if not all keys are in upper case or lower case
    return False
