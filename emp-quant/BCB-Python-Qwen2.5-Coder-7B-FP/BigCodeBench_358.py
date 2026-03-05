import itertools
import json
def task_func(json_list, r):
    try:
        # Load the JSON data from the input string
        data = json.loads(json_list)
        
        # Check if the 'number_list' key exists in the JSON data
        if 'number_list' not in data:
            raise Exception("The JSON data does not contain the 'number_list' key.")
        
        # Extract the number list from the JSON data
        number_list = data['number_list']
        
        # Check if the number list is empty
        if not number_list:
            raise Exception("The 'number_list' is empty.")
        
        # Generate all possible combinations of r elements from the number list
        combinations = list(itertools.combinations(number_list, r))
        
        return combinations
    
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")