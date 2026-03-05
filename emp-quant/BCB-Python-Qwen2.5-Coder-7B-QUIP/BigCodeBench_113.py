
import json
from collections import Counter
import random

def task_func(my_dict, keys):
    if len(keys) != 10 or len(Counter(keys)) != 10:
        raise ValueError("The 'keys' parameter must contain exactly 10 unique elements.")
    
    # Add 10 random elements to the dictionary
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    
    # Save the dictionary to a JSON file
    json_path = 'updated_dictionary.json'
    with open(json_path, 'w') as f:
        json.dump(my_dict, f)
    
    # Save the counts of each key to a text file
    key_counts = {key: my_dict[key] for key in keys}
    txt_path = 'key_frequencies.txt'
    with open(txt_path, 'w') as f:
        for key, count in key_counts.items():
            f.write(f"{key}: {count}\n")
    
    return my_dict, json_path, txt_path