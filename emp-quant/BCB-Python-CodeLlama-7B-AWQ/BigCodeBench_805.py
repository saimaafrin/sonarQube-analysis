import pandas as pd
import random
def task_func(dictionary, item, seed):
    """
    Converts a dictionary to a pandas DataFrame and finds the locations of a particular item in the resulting DataFrame.
    Counts the number of occurences and adds a random integer x, where 0 <=x < 10, to it.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(dictionary)

    # Find the locations of the item in the DataFrame
    locations = df.stack().str.contains(item).nonzero()

    # Count the number of occurences and add a random integer x, where 0 <=x < 10
    count = locations.shape[0]
    random_number = random.randint(0, 10)
    count += random_number

    # Return a list of tuples containing the row-index and column-name where the item is found
    return [(row, col) for row, col in zip(locations[0], locations[1])]
item = 'e'
seed = 2