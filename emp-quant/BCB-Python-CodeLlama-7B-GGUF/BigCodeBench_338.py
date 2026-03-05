
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        formatted_elements.append('%s%s' % (random_string, element))
    # Create histogram of character occurrences
    char_counts = {}
    for formatted_element in formatted_elements:
        for char in formatted_element:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1
    # Plot histogram
    plt.bar(range(len(char_counts)), char_counts.values())
    plt.xlabel('Character')
    plt.ylabel('Count')
    plt.title('Histogram of Character Occurrences')
    return formatted_elements, plt.gca(), char_counts