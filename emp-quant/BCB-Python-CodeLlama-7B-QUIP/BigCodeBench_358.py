
import itertools
import json

def task_func(json_list, r):
    # Check if the input is a valid JSON
    try:
        json_data = json.loads(json_list)
    except ValueError:
        raise ValueError("Invalid JSON")

    # Check if the input is not empty
    if not json_data:
        raise ValueError("Empty JSON")

    # Check if the input has the 'number_list' key
    if 'number_list' not in json_data:
        raise ValueError("JSON does not have 'number_list' key")

    # Extract the number list from the JSON data
    number_list = json_data['number_list']

    # Generate all possible combinations of r elements from the number list
    combinations = itertools.combinations(number_list, r)

    # Return the list of tuples
    return list(combinations)