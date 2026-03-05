import string
import matplotlib.pyplot as plt
def task_func(s):
    """
    Calculate the frequency of each letter in a string and return a bar chart of frequencies. Results are case-insensitive. If non-string input is provided, function will throw an error.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Create a dictionary to store the frequency of each letter
    freq = {}

    # Iterate over each letter in the string
    for c in s.lower():
        # If the letter is not in the dictionary, add it with a frequency of 1
        if c not in freq:
            freq[c] = 1
        # Otherwise, increment the frequency of the letter
        else:
            freq[c] += 1

    # Create a bar plot of the letter frequencies
    plt.bar(freq.keys(), freq.values())
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequencies")
    plt.show()

    # Return the dictionary of letter frequencies
    return freq
s = "Hello, World!"