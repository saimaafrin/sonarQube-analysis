import numpy as np
import datetime
def task_func(arr):
    """
    Reverse the order of words separated by "." in all strings of a numpy array.
    """
    # Initialize an empty list to store the reversed strings
    reversed_strings = []

    # Iterate over the strings in the input array
    for string in arr:
        # Split the string into words using "." as the delimiter
        words = string.split(".")

        # Reverse the order of the words
        reversed_words = words[::-1]

        # Join the reversed words back into a string using "." as the delimiter
        reversed_string = ".".join(reversed_words)

        # Add the reversed string to the list
        reversed_strings.append(reversed_string)

    # Return the list of reversed strings as a numpy array
    return np.array(reversed_strings)
arr = np.array(["This is a test.", "This is another test."])