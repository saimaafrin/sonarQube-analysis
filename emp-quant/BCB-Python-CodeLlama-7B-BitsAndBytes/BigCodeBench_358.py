
import itertools
import json

def task_func(json_list, r):
    # Check if the input is a valid JSON string
    try:
        json_data = json.loads(json_list)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string")

    # Check if the JSON data has the 'number_list' key
    if 'number_list' not in json_data:
        raise KeyError("JSON data does not have 'number_list' key")

    # Extract the number list from the JSON data
    number_list = json_data['number_list']

    # Generate all possible combinations of r elements from the number list
    combinations = itertools.combinations(number_list, r)

    # Return the list of tuples representing the combinations
    return list(combinations)