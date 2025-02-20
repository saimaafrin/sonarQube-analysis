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

    # 1. if dict is empty, return False
    if not dict:
        return False
    # 2. get keys
    keys = list(dict.keys())
    # 3. get first key
    first_key = keys[0]
    # 4. check if key is str
    if not isinstance(first_key, str):
        return False
    # 5. check if key is all lowercase
    is_all_lowercase = all(x.islower() for x in keys)
    # 6. check if key is all uppercase
    is_all_uppercase = all(x.isupper() for x in keys)
    # 7. if key is not all lowercase and is not all uppercase, return False
    if not is_all_lowercase and not is_all_uppercase:
        return False
    # 8. else, return True
    return True
