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
    if len(dict) == 0:
        return False
    
    # Get the first key
    key = list(dict.keys())[0]

    # Check if the first key is in upper case
    if key.isupper():
        # Check if all keys are in upper case
        return all(key.isupper() for key in dict.keys())
    # Check if the first key is in lower case
    elif key.islower():
        # Check if all keys are in lower case
        return all(key.islower() for key in dict.keys())
    # The key is neither in upper or lower case
    else:
        return False
