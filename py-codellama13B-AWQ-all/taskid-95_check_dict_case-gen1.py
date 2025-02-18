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

    # Check if the dict is empty
    if len(dict) == 0:
        return False

    # Check if the first key is in lower case or upper case
    if dict[list(dict.keys())[0]].islower():
        is_lower_case = True
    else:
        is_lower_case = False

    # Check if all the keys are in the same case
    for key in dict.keys():
        if dict[key].islower():
            if not is_lower_case:
                return False
        else:
            if is_lower_case:
                return False

    return True
