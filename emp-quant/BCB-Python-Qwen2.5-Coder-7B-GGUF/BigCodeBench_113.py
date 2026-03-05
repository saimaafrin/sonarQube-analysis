
import json
from collections import Counter
import random

def task_func(my_dict, keys):
    if len(keys) != 10 or len(set(keys)) != 10:
        raise ValueError("The 'keys' parameter must contain exactly 10 unique elements.")
    
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    
    json_path = 'updated_dictionary.json'
    with open(json_path, 'w') as json_file:
        json.dump(my_dict, json_file)
    
    txt_path = 'key_frequencies.txt'
    key_counts = Counter(my_dict)
    with open(txt_path, 'w') as txt_file:
        for key, count in key_counts.items():
            txt_file.write(f"{key}: {count}\n")
    
    return my_dict, json_path, txt_path