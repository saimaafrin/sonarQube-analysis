import random
import string
import pandas as pd
def task_func(data_list, seed=0):
    """
    Replace a random substring (a sequence of characters between two commas or at the beginning/end of the string) in a list of strings with a random string (comprising ascii lowercase characters) with the same length as the substituted characters.
    """
    random.seed(seed)
    modified_list = []
    for data in data_list:
        # Find the index of the first comma
        first_comma_index = data.find(",")
        # If there is no comma, return the original string
        if first_comma_index == -1:
            modified_list.append(data)
            continue
        # Find the index of the second comma
        second_comma_index = data.find(",", first_comma_index + 1)
        # If there is no second comma, return the original string
        if second_comma_index == -1:
            modified_list.append(data)
            continue
        # Replace the substring with a random string
        random_string = "".join(random.choice(string.ascii_lowercase) for _ in range(second_comma_index - first_comma_index))
        modified_list.append(data[:first_comma_index] + random_string + data[second_comma_index + 1:])
    return pd.DataFrame({"Original String": data_list, "Modified String": modified_list})
data_list = ["Hello,World", "Hello,Python", "Hello,Pandas"]