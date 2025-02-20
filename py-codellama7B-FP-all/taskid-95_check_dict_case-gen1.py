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

    # If the dictionary is empty, return False
    if not dict: return False
    # If there is at least one key that is in upper case, return False
    if any(key.isupper() for key in dict.keys()):
        return False
    # If there is at least one key that is not in lower case, return False
    if any(not key.islower() for key in dict.keys()):
        return False
    # If we made it this far, all keys are in lower case, return True
    return True
