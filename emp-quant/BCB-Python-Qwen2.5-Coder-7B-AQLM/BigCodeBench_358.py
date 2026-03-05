
import itertools
import json

def task_func(json_list, r):
    try:
        # Load the JSON data
        data = json.loads(json_list)
        
        # Check if the data is empty or does not contain 'number_list' key
        if not data or 'number_list' not in data:
            raise Exception("Invalid JSON or missing 'number_list' key")
        
        # Extract the number list
        number_list = data['number_list']
        
        # Generate all possible combinations of r elements
        combinations = list(itertools.combinations(number_list, r))
        
        return combinations
    
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format")