from collections import Counter
import json
import random
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Select n random words from the WORDS list
    selected_words = random.sample(WORDS, n)
    
    # Create a dictionary with the selected words and their counts
    word_counts = dict(Counter(selected_words))
    
    # Write the dictionary to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(word_counts, json_file)
    
    # Return the name of the JSON file generated
    return file_name