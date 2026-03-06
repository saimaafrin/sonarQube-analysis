
import json
from collections import Counter
import random

def task_func(my_dict, keys):
    if len(set(keys)) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")

    # Add 10 random elements to the dictionary
    for i in range(10):
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

    return my_dict, "updated_dictionary.json", "key_frequencies.txt"