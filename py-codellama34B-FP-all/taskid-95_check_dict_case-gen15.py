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


    # check dictionary is empty
    if not dict:
        return False

    # if first element of dictionary is in upper case
    if dict[list(dict)[0]].isupper():
        # check all keys are in upper case
        for k in dict:
            if k.isupper() is False:
                return False
    # if first element of dictionary is in lower case
    elif dict[list(dict)[0]].islower():
        # check all keys are in lower case
        for k in dict:
            if k.islower() is False:
                return False

    return True
