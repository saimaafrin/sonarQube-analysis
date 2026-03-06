
import string
import matplotlib.pyplot as plt

def task_func(s):
    # Check if input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Convert string to lowercase
    s = s.lower()

    # Create a dictionary to store letter frequencies
    freq = {}

    # Iterate through each letter in the string
    for letter in s:
        # Check if letter is in the dictionary
        if letter in freq:
            # Increment the frequency of the letter
            freq[letter] += 1
        else:
            # Add the letter to the dictionary with frequency of 1
            freq[letter] = 1

    # Create a bar plot of letter frequencies
    plt.bar(freq.keys(), freq.values())
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequencies")

    # Return the dictionary and the bar plot
    return freq, plt.gca()