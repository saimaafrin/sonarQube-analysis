from collections import Counter
import json
import random
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    """
    Generate a json file with n randomly selected words from the WORDS constant list.
    """
    # Set the random seed for reproducibility
    random.seed(seed)
    # Generate a list of n random words
    random_words = random.sample(WORDS, n)
    # Create a dictionary with the random words as keys and their counts as values
    word_counts = Counter(random_words)
    # Write the dictionary to a json file
    with open(file_name, 'w') as f:
        json.dump(word_counts, f)
    # Return the name of the json file
    return file_name