from collections import Counter
import json
import random
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Select n random words from the WORDS list
    selected_words = random.sample(WORDS, n)
    
    # Create a dictionary to count occurrences of each word
    word_count = Counter(selected_words)
    
    # Create a JSON object from the word count dictionary
    json_object = json.dumps(word_count, indent=4)
    
    # Write the JSON object to a file
    with open(file_name, 'w') as file:
        file.write(json_object)
    
    # Return the name of the file generated
    return file_name