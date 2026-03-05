import string
import matplotlib.pyplot as plt
def task_func(s):
    """
    Calculate the frequency of each letter in a string and return a bar chart of frequencies. Results are case-insensitive. If non-string input is provided, function will throw an error.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Create a dictionary to store the frequency of each letter
    letter_freq = {}

    # Iterate over each letter in the string
    for letter in s:
        # Check if the letter is in the dictionary
        if letter in letter_freq:
            # Increment the frequency of the letter
            letter_freq[letter] += 1
        else:
            # Add the letter to the dictionary with a frequency of 1
            letter_freq[letter] = 1

    # Create a list of tuples containing the letter and its frequency
    letter_freq_list = [(letter, freq) for letter, freq in letter_freq.items()]

    # Sort the list by frequency in descending order
    letter_freq_list.sort(key=lambda x: x[1], reverse=True)

    # Create a bar plot of the letter frequencies
    plt.bar(letter_freq_list, xlabel="Letters", ylabel="Frequency")

    # Return the dictionary and the bar plot
    return letter_freq, plt.gca()
s = "Hello, World!"