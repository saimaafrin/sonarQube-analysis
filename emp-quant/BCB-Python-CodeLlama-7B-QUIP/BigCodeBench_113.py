
import json
from collections import Counter
import random

def task_func(my_dict, keys):
    if len(keys) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    with open("updated_dictionary.json", "w") as json_file:
        json.dump(my_dict, json_file)
    with open("key_frequencies.txt", "w") as text_file:
        for key, count in Counter(my_dict).items():
            text_file.write(f"{key}: {count}\n")
    return my_dict, "updated_dictionary.json", "key_frequencies.txt"