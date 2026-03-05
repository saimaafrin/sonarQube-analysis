import itertools
import json
def task_func(json_list, r):
    """
    Generate all possible combinations of r elements from a given number list taken from JSON string input.
    Note that:
        - The datetime to be extracted is located in the 'number_list' key in the JSON data.
        - The function should raise the exception for:
            - Raise an Exception if the json_list is an invalid JSON, empty, or does not have 'number_list' key.
        - The function should output with:
            - list: A list of tuples, each tuple representing a combination.
    """
    try:
        json_data = json.loads(json_list)
        number_list = json_data['number_list']
    except (json.JSONDecodeError, KeyError):
        raise Exception('Invalid JSON or missing "number_list" key')

    if not number_list:
        raise Exception('Empty "number_list"')

    if r > len(number_list):
        raise Exception(f'r ({r}) is greater than the length of number_list ({len(number_list)})')

    combinations = itertools.combinations(number_list, r)
    return list(combinations)
json_list = '{"number_list": [1, 2, 3, 4, 5]}'
r = 3