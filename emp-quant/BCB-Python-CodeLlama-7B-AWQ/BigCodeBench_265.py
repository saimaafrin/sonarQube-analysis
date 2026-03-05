import collections
import json
import os
def task_func(data, json_file_name='data.json'):
    """
    Add a new key "a" with the value 1 to the input dictionary, calculate the frequency of its values, and save the updated dictionary along with its frequency distribution to a JSON file.
    The dictionary is saved under the key 'data' and the frequency distribution under the key 'freq'.
    The function should output with:
        str: The path of the JSON file.
    """
    # Add the new key "a" with the value 1 to the input dictionary
    data['a'] = 1

    # Calculate the frequency of the values in the dictionary
    freq = collections.Counter(data.values())

    # Save the updated dictionary and its frequency distribution to a JSON file
    with open(json_file_name, 'w') as f:
        json.dump({'data': data, 'freq': freq}, f)

    # Return the path of the JSON file
    return os.path.abspath(json_file_name)
data = {'a': 1, 'b': 2, 'c': 3}
json_file_name = 'data.json'