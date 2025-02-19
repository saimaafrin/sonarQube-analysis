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


    # Empty dictionary
    if not dict:
        return False

    # First character of the first key is the key to compare
    # to the rest of the keys
    key_to_compare = list(dict)[0][0]

    # Checks each key against the first key. If one key is not equal
    # to the first key, return False
    for key in dict:
        if key[0] != key_to_compare:
            return False

    return True
