import itertools
import json
def task_func(json_list, r):
    # Check if the input is a valid JSON string
    try:
        data = json.loads(json_list)
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input")
    
    # Check if the JSON data is empty
    if not data:
        raise Exception("Empty JSON input")
    
    # Check if the 'number_list' key exists in the JSON data
    if 'number_list' not in data:
        raise Exception("JSON input does not contain 'number_list' key")
    
    # Extract the number list from the JSON data
    number_list = data['number_list']
    
    # Generate all possible combinations of r elements from the number list
    combinations = list(itertools.combinations(number_list, r))
    
    return combinations