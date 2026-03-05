
import json
from collections import Counter
import random

def task_func(my_dict, keys):
    if len(keys) != 10:
        raise ValueError("'keys' must contain exactly 10 unique elements")
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    with open("updated_dictionary.json", "w") as f:
        json.dump(my_dict, f)
    with open("key_frequencies.txt", "w") as f:
        for key, count in Counter(my_dict).items():
            f.write(f"{key}: {count}\n")
    return my_dict, "updated_dictionary.json", "key_frequencies.txt"