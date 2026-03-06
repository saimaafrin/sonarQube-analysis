
import collections
import json
import os

def task_func(data, json_file_name='data.json'):
    # Add a new key "a" with the value 1 to the input dictionary
    data['a'] = 1
    
    # Calculate the frequency of its values
    freq = collections.Counter(data.values())
    
    # Save the updated dictionary along with its frequency distribution to a JSON file
    result_dict = {'data': data, 'freq': dict(freq)}
    with open(json_file_name, 'w') as f:
        json.dump(result_dict, f)
    
    # Output the path of the JSON file
    return json_file_name