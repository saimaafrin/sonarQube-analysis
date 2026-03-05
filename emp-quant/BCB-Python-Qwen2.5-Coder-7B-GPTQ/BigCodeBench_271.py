import random
import string
import hashlib
import time
def task_func(data_dict: dict, seed=0) -> dict:
    # Set the seed for random number generation
    random.seed(seed)
    
    # Add a key "a" with a value of 1
    data_dict["a"] = 1
    
    # Generate a random salt of length 5 using lowercase ASCII letters
    salt = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # For each key-value pair in the dictionary, concatenate the value with the generated salt,
    # hash the concatenated string using SHA-256, and update the value with the hashed string
    for key in list(data_dict.keys()):
        if key != "a":  # Skip the key "a" that was added
            value = data_dict[key]
            concatenated = str(value) + salt
            hashed_value = hashlib.sha256(concatenated.encode()).hexdigest()
            data_dict[key] = hashed_value
    
    # Add a 'timestamp' key with the current UNIX timestamp as its value
    data_dict['timestamp'] = int(time.time())
    
    return data_dict