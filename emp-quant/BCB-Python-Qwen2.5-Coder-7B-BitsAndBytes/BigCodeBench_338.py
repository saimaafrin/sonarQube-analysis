
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    random.seed(seed)
    
    # Format each string in the list with a random alphanumeric string of length 5
    formatted_elements = [f"%{random.choices(string.ascii_letters + string.digits, k=5)}%" for _ in elements]
    
    # Concatenate all formatted strings to count characters
    all_chars = ''.join(formatted_elements)
    
    # Count the occurrences of each character
    char_count = {}
    for char in all_chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Create a histogram of character occurrences
    fig, ax = plt.subplots()
    ax.bar(char_count.keys(), char_count.values())
    ax.set_xlabel('Characters')
    ax.set_ylabel('Occurrences')
    ax.set_title('Character Occurrences in Formatted Strings')
    
    return formatted_elements, ax, char_count