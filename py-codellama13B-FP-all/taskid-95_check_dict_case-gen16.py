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

    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Check if the dictionary keys are strings
    if not all(isinstance(k, str) for k in dict):
        return False
    
    # Check if all keys are in lower case or all keys are in upper case
    if not all(k.islower() for k in dict) and not all(k.isupper() for k in dict):
        return False
    
    # Otherwise, all keys are in the same case
    return True
