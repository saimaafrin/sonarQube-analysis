import random
import string
import pandas as pd
def task_func(data_list, seed=0):
    """
    Replace a random substring (a sequence of characters between two commas or at the beginning/end of the string) in a list of strings with a random string (comprising ascii lowercase characters) with the same length as the substituted characters.
    The function should output with:
        DataFrame: A pandas DataFrame with two columns - 'Original String' and 'Modified String'.
        'Original String' contains the original strings from the input list, and 'Modified String'
        contains the modified strings where a random substring has been replaced.
    """
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a list of original strings
    original_strings = data_list

    # Create a list of modified strings
    modified_strings = []

    # Loop through each original string
    for original_string in original_strings:
        # Split the original string into a list of substrings
        substrings = original_string.split(',')

        # Create a new list of substrings with random characters
        new_substrings = []
        for substring in substrings:
            # Get the length of the substring
            substring_length = len(substring)

            # Create a random string with the same length as the substring
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(substring_length))

            # Add the random string to the new list of substrings
            new_substrings.append(random_string)

        # Join the new list of substrings into a single string
        modified_string = ','.join(new_substrings)

        # Add the modified string to the list of modified strings
        modified_strings.append(modified_string)

    # Create a DataFrame with the original and modified strings
    df = pd.DataFrame({'Original String': original_strings, 'Modified String': modified_strings})

    return df
data_list = ['hello,world', 'goodbye,cruel,world', 'foo,bar,baz']