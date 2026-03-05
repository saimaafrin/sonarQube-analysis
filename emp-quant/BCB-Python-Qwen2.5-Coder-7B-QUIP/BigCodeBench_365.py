
from collections import Counter
import json
import random
# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Select n random words from the WORDS list
    selected_words = random.sample(WORDS, n)
    
    # Create a dictionary with the selected words
    data = {'selected_words': selected_words}
    
    # Write the dictionary to a JSON file
    with open(file_name, 'w') as f:
        json.dump(data, f)
    
    # Return the name of the file generated
    return file_name