import json
from collections import Counter
import random
def task_func(my_dict, keys):
    """
    Updates a given dictionary by adding 10 random elements based on the 'keys' parameter, with values as random integers from 1 to 100. It saves the JSON representation of the updated dictionary to a file and the counts of each key to a separate text file.
    Note that:
        - This function modifies the input dictionary in place.
        - The filename of the json is 'updated_dictionary.json'
        - The filename of the txt file is 'key_frequencies.txt'
    The function should raise the exception for:
        - ValueError: If 'keys' does not contain exactly 10 unique elements.
    The function should output with:
        - tuple: The dictionary, path to the JSON file, and path to the text file.
    """
    # Check if 'keys' contains exactly 10 unique elements
    if len(keys) != 10 or len(set(keys)) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")

    # Add 10 random elements to the dictionary
    for _ in range(10):
        key = random.choice(keys)
        value = random.randint(1, 100)
        my_dict[key] = value

    # Save the updated dictionary to a JSON file
    with open("updated_dictionary.json", "w") as f:
        json.dump(my_dict, f)

    # Save the counts of each key to a text file
    with open("key_frequencies.txt", "w") as f:
        for key, value in Counter(my_dict).items():
            f.write(f"{key}: {value}\n")

    # Return the updated dictionary, path to the JSON file, and path to the text file
    return my_dict, "updated_dictionary.json", "key_frequencies.txt"
my_dict = {"a": 1, "b": 2, "c": 3}
keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]