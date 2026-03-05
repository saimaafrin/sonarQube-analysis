import string
import matplotlib.pyplot as plt
def task_func(s):
    """
    Calculate the frequency of each letter in a string and return a bar chart of frequencies. Results are case-insensitive. If non-string input is provided, function will throw an error.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Create a dictionary to store the frequency of each letter
    freq = {}

    # Iterate over each letter in the string
    for letter in s:
        # Convert the letter to lowercase
        letter = letter.lower()

        # If the letter is not in the dictionary, add it with a frequency of 1
        if letter not in freq:
            freq[letter] = 1
        # Otherwise, increment the frequency of the letter
        else:
            freq[letter] += 1

    # Create a list of tuples containing the letter and its frequency
    freq_list = [(letter, freq[letter]) for letter in freq]

    # Sort the list by frequency in descending order
    freq_list.sort(key=lambda x: x[1], reverse=True)

    # Create a bar plot of the letter frequencies
    plt.bar(freq_list, xlabel="Letters", ylabel="Frequency")
    plt.title("Letter Frequencies")
    plt.show()

    # Return the dictionary and the bar plot
    return freq, plt.gca()
s = "Hello, World!"