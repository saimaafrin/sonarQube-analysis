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

    # get the first key and it's value
    first_key = list(dict.keys())[0]
    first_value = dict[first_key]

    # Check if all keys are the same case as the first key
    for key in dict:
        if key.islower() and not first_key.islower():
            return False
        elif key.isupper() and not first_key.isupper():
            return False
    
    return True
