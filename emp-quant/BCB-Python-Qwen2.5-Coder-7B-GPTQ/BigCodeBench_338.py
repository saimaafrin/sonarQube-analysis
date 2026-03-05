import random
import string
from collections import Counter
from matplotlib import pyplot as plt
def task_func(elements, seed=100):
    random.seed(seed)
    formatted_elements = []
    char_count = Counter()
    
    for element in elements:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        formatted_element = f"% {element} %"
        formatted_elements.append(formatted_element)
        
        # Update character count
        for char in formatted_element:
            char_count[char] += 1
    
    # Plot histogram
    plt.figure(figsize=(10, 5))
    plt.bar(char_count.keys(), char_count.values(), color='blue')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Character Frequency in Formatted Strings')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return formatted_elements, plt.gca(), dict(char_count)
elements = ["apple", "banana", "cherry"]