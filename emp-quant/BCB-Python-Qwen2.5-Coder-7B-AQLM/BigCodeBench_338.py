
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    random.seed(seed)
    formatted_elements = []
    char_count = {}

    for element in elements:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        formatted_element = f"% {random_string}%"
        formatted_elements.append(formatted_element)

        for char in formatted_element:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(char_count.keys(), char_count.values())
    plt.xlabel('Characters')
    plt.ylabel('Count')
    plt.title('Character Count in Formatted Strings')
    plt.show()

    return formatted_elements, plt.gca(), char_count