from collections import defaultdict
import itertools
import json
import random
def task_func(LETTERS, n):
    # Generate all possible combinations of length 'n'
    combinations = list(itertools.combinations(LETTERS, n))
    
    # Count occurrences of each letter in these combinations
    letter_counts = defaultdict(int)
    for combo in combinations:
        for letter in combo:
            letter_counts[letter] += 1
    
    # Generate a random number between 0 and 100 for the file name
    random_number = random.randint(0, 100)
    
    # Create the file name
    file_name = f"prefix_{random_number}.json"
    
    # Save the results in a JSON file
    with open(file_name, 'w') as f:
        json.dump(dict(letter_counts), f)
    
    # Return the name of the generated JSON file
    return file_name