import itertools
import json
def task_func(json_list, r):
    """
    Generate all possible combinations of r elements from a given number list taken from JSON string input.
    Note that: The datetime to be extracted is located in the 'number_list' key in the JSON data.
    The function should raise the exception for: Raise an Exception if the json_list is an invalid JSON, empty, or does not have 'number_list' key.
    The function should output with:
        list: A list of tuples, each tuple representing a combination.
    """
    # Check if the input is a valid JSON
    try:
        json_data = json.loads(json_list)
    except json.JSONDecodeError:
        raise Exception("Invalid JSON")

    # Check if the JSON data is empty
    if not json_data:
        raise Exception("JSON data is empty")

    # Check if the JSON data has the 'number_list' key
    if "number_list" not in json_data:
        raise Exception("JSON data does not have 'number_list' key")

    # Extract the number list from the JSON data
    number_list = json_data["number_list"]

    # Generate all possible combinations of r elements from the number list
    combinations = itertools.combinations(number_list, r)

    # Return the list of tuples representing the combinations
    return list(combinations)
json_list = '{"number_list": [1, 2, 3, 4, 5]}'
r = 3