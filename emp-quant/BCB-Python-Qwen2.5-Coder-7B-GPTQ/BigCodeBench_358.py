import itertools
import json
def task_func(json_list, r):
    try:
        data = json.loads(json_list)
        if not data or 'number_list' not in data:
            raise ValueError("Invalid JSON or missing 'number_list' key")
        
        number_list = data['number_list']
        if not number_list:
            raise ValueError("Empty 'number_list'")
        
        return list(itertools.combinations(number_list, r))
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")