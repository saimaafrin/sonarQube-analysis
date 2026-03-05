
import pandas as pd
import random

def task_func(dictionary, item, seed):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary)

    # Find locations of item in DataFrame
    locations = df.stack().index[df.stack() == item].tolist()

    # Add random integer to each location
    random.seed(seed)
    for location in locations:
        location = (location[0], location[1], random.randint(0, 10))

    # Count number of occurences
    count = len(locations)

    # Return list of tuples, number of occurences, and DataFrame
    return locations, count, df