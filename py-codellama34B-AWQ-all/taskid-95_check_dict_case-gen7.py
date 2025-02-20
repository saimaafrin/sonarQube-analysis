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


    # If dictionary is empty, return False.
    if len(dict) == 0:
        return False

    # If dictionary contains only strings in upper case, return True.
    if all(key.isupper() for key in dict.keys()):
        return True

    # If dictionary contains only strings in lower case, return True.
    if all(key.islower() for key in dict.keys()):
        return True

    # If dictionary does not contain only strings in upper or lower case, return False.
    return False
