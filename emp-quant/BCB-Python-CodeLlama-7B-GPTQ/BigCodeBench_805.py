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

    # Count the number of occurences
    count = locations.size

    # Add a random integer x, where 0 <=x < 10, to the count
    x = random.randint(0, 9)
    count += x

    # Return the list of tuples, the number of occurences, and the DataFrame
    return list(locations), count, df
item = 'e'
seed = 2