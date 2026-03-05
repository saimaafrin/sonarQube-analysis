import random
import string
import matplotlib.pyplot as plt
def task_func(elements, seed=100):
    """
    Format each string in the given list "elements" into a pattern "% {0}%", where {0} is a randomly generated alphanumeric string of length 5.
    Additionally, return the plot axes of an histogram of the occurrence of each character across all the strings and a dictionary containing the count of each character in all the formatted strings.
    """
    random.seed(seed)
    formatted_elements = []
    char_counts = {}
    for element in elements:
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        formatted_element = f"% {random_string}%"
        formatted_elements.append(formatted_element)
        for char in formatted_element:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1
    # Plot the histogram of the occurrence of each character across all the strings
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(char_counts)), char_counts.values(), align='center')
    plt.xticks(range(len(char_counts)), char_counts.keys())
    plt.xlabel('Character')
    plt.ylabel('Count')
    plt.title('Histogram of characters in formatted strings')
    plt.show()
    return formatted_elements, plt.gca(), char_counts
elements = ['apple', 'banana', 'cherry']