import random
import string
import pandas as pd
def task_func(data_list, seed=0):
    """
    Replace a random substring (a sequence of characters between two commas or at the beginning/end of the string) in a list of strings with a random string (comprising ascii lowercase characters) with the same length as the substituted characters.
    """
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a list to store the original and modified strings
    original_strings = []
    modified_strings = []

    # Iterate over the input list of strings
    for s in data_list:
        # Split the string into a list of substrings
        substrings = s.split(",")

        # Choose a random substring to replace
        replace_index = random.randint(0, len(substrings) - 1)

        # Generate a random string with the same length as the substituted substring
        replace_string = "".join(random.choice(string.ascii_lowercase) for _ in range(len(substrings[replace_index])))

        # Replace the chosen substring with the random string
        substrings[replace_index] = replace_string

        # Join the list of substrings back into a string
        modified_string = ",".join(substrings)

        # Add the original and modified strings to the output lists
        original_strings.append(s)
        modified_strings.append(modified_string)

    # Create a pandas DataFrame with the original and modified strings
    df = pd.DataFrame({"Original String": original_strings, "Modified String": modified_strings})

    return df
data_list = ["apple,banana,orange", "grape,strawberry,raspberry", "pineapple,mango,pineapple"]