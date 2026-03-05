
import collections
import json
import os

def task_func(data, json_file_name='data.json'):
    # Add a new key "a" with the value 1 to the input dictionary
    data['a'] = 1
    
    # Calculate the frequency of its values
    freq = collections.Counter(data.values())
    
    # Save the updated dictionary along with its frequency distribution to a JSON file
    output_data = {
        'data': data,
        'freq': dict(freq)
    }
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(json_file_name), exist_ok=True)
    
    # Write the data to a JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
    
    # Return the path of the JSON file
    return json_file_name