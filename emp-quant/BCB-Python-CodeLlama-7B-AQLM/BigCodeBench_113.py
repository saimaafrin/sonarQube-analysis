import json
from collections import Counter
import random
def task_func(my_dict, keys):
    """
    Updates a given dictionary by adding 10 random elements based on the 'keys' parameter,
    with values as random integers from 1 to 100. It saves the JSON representation of the
    updated dictionary to a file and the counts of each key to a separate text file.

    Parameters:
        my_dict (dict): The dictionary to be updated.
        keys (list of str): A list of keys to be added to the dictionary.

    Returns:
        tuple: The dictionary, path to the JSON file, and path to the text file.

    Raises:
        ValueError: If 'keys' does not contain exactly 10 unique elements.

    Note:
        This function modifies the input dictionary in place.
        The filename of the json is 'updated_dictionary.json'
        The filename of the txt file is 'key_frequencies.txt'

    Requirements:
    - json
    - collections.Counter
    - random

    Examples:
    >>> result, json_path, txt_path = task_func({'first_key': 1, 'second_key': 2}, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    >>> isinstance(result, dict)
    True
    >>> len(result) > 2  # Checking if more keys have been added
    True
    """
    if len(keys) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")
    if len(set(keys)) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    with open('updated_dictionary.json', 'w') as f:
        json.dump(my_dict, f)
    with open('key_frequencies.txt', 'w') as f:
        for key, value in Counter(keys).items():
            f.write(f'{key}: {value}\n')
    return my_dict, 'updated_dictionary.json', 'key_frequencies.txt'