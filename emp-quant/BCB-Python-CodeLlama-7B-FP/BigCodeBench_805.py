import pandas as pd
import random
def task_func(dictionary, item, seed):
    """
    Converts a dictionary to a pandas DataFrame and finds the locations of a particular item in the resulting DataFrame.
    Counts the number of occurences and adds a random integer x, where 0 <=x < 10, to it.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(dictionary)

    # Find the locations of the item in the DataFrame
    locations = df.stack().str.contains(item).nonzero()

    # Count the number of occurences and add a random integer x, where 0 <=x < 10
    num_occurences = locations.shape[0]
    random_integer = random.randint(0, 10)
    num_occurences += random_integer

    # Return a list of tuples containing the row-index and column-name where the item is found
    return [(row_index, column_name) for row_index, column_name in locations], num_occurences, df
item = 'e'
seed = 2