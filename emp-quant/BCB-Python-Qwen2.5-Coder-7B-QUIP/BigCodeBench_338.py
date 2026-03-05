
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    # Set the seed for random number generation
    random.seed(seed)

    # Generate a random alphanumeric string of length 5
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Format each string in the list with the random pattern
    formatted_elements = [f"{random_string} {element} {random_string}" for element in elements]

    # Initialize a dictionary to count the occurrences of each character
    char_count = {}

    # Iterate over the formatted elements and count the characters
    for element in formatted_elements:
        for char in element:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Plot the histogram of the occurrence of each character
    plt.figure()
    plt.bar(range(len(char_count)), list(char_count.values()), align='center')
    plt.xticks(range(len(char_count)), list(char_count.keys()))
    plt.xlabel('Character')
    plt.ylabel('Count')
    plt.title('Character Count Histogram')

    # Return the formatted list, the axes object, and the character count dictionary
    return formatted_elements, plt.gca(), char_count