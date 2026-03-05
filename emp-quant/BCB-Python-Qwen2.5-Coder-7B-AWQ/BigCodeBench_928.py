from collections import Counter
import itertools
import string
def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations of the lowercase English alphabet
    alphabet = string.ascii_lowercase
    combinations = [''.join(p) for p in itertools.product(alphabet, repeat=2)]
    
    # Initialize a counter for the word
    word_counter = Counter(word)
    
    # Create a dictionary to store the frequency of each combination
    result = {combo: 0 for combo in combinations}
    
    # Count the occurrences of each combination in the word
    for combo in combinations:
        for i in range(len(word) - 1):
            if word[i:i+2] == combo:
                result[combo] += 1
    
    return result