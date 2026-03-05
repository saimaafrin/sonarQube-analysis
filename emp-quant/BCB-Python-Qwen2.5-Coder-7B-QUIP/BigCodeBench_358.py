
import itertools
import json
def task_func(json_list, r):
    # Validate the JSON input
    if not json_list:
        raise Exception("Input JSON list is empty")
    try:
        data = json.loads(json_list)
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input")
    
    # Check if 'number_list' key exists in the JSON data
    if 'number_list' not in data:
        raise Exception("Input JSON does not contain 'number_list' key")
    
    # Extract the number list from the JSON data
    number_list = data['number_list']
    
    # Generate all combinations of r elements from the number list
    combinations = list(itertools.combinations(number_list, r))
    
    # Output the list of combinations
    return list(combinations)