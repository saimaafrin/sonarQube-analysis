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


    # If the dictionary has no keys, return False
    if not dict:
        return False

    # Determine if the dictionary contains only uppercase or lowercase keys
    is_lowercase = True
    is_uppercase = True

    for key in dict.keys():
        if not key.islower():
            is_lowercase = False
        if not key.isupper():
            is_uppercase = False
    
    # Return True if the dictionary contains only uppercase or lowercase keys
    if is_lowercase or is_uppercase:
        return True
    else:
        return False
