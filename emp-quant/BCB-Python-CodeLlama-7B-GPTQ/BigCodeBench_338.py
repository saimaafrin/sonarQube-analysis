import random
import string
from matplotlib import pyplot as plt
def task_func(elements, seed=100):
    """
    Format each string in the given list "elements" into a pattern "% {0}%", where {0} is a randomly generated alphanumeric string of length 5. Additionally, return the plot axes of an histogram of the occurrence of each character across all the strings and a dictionary containing the count of each character in all the formatted strings.
    """
    # Generate a random seed for reproducibility
    random.seed(seed)

    # Create a list of formatted strings
    formatted_elements = []
    for element in elements:
        # Generate a random alphanumeric string of length 5
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        # Format the element with the random string
        formatted_element = f"% {random_string}%"
        formatted_elements.append(formatted_element)

    # Create a dictionary to store the count of each character in the formatted strings
    char_counts = {}
    for formatted_element in formatted_elements:
        for char in formatted_element:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1

    # Create a histogram plot of the occurrence of each character across all the strings
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(char_counts)), list(char_counts.values()))
    plt.xlabel("Character")
    plt.ylabel("Count")
    plt.title("Histogram of Character Occurrence in Formatted Strings")
    plt.show()

    return formatted_elements, plt.gca(), char_counts
elements = ["apple", "banana", "cherry"]