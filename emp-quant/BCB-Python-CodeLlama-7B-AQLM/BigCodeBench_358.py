import itertools
import json
def task_func(json_list, r):
    """
    Generate all possible combinations of r elements from a given number list taken from JSON string input.
    
    Parameters:
    json_list (str): JSON string containing the number list.
    r (int): The number of elements in each combination.

    Returns:
    list: A list of tuples, each tuple representing a combination.

    Note:
    - The datetime to be extracted is located in the 'number_list' key in the JSON data.

    Raises:
    - Raise an Exception if the json_list is an invalid JSON, empty, or does not have 'number_list' key.
    
    Requirements:
    - itertools
    - json
    
    Example:
    >>> combinations = task_func('{"number_list": [1, 2, 3, 4, 5]}', 3)
    >>> print(combinations)
    [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    """
    try:
        json_data = json.loads(json_list)
    except Exception as e:
        raise Exception(f'Invalid JSON: {e}')

    if not json_data or 'number_list' not in json_data:
        raise Exception('Invalid JSON: Missing "number_list" key')

    number_list = json_data['number_list']

    if not number_list:
        raise Exception('Invalid JSON: Empty "number_list"')

    if r > len(number_list):
        raise Exception(f'Invalid r: {r}')

    return list(itertools.combinations(number_list, r))