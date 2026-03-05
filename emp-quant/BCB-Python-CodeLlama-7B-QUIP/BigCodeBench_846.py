
import collections
import pandas as pd

def task_func(obj_list, attr):
    # Create a dictionary to store the counts for each attribute
    counts = collections.Counter()

    # Loop through the objects in the list
    for obj in obj_list:
        # Get the value of the attribute for this object
        value = getattr(obj, attr)

        # If the attribute is not None, increment the count for this value
        if value is not None:
            counts[value] += 1

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(counts, columns=['attribute', 'count'])

    return df