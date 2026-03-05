import collections
import pandas as pd
def task_func(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    This function returns a pandas Dataframe containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consist of two columns ('attribute' and 'count'), which contain the attribute and its specific count respectively.
    If no attributes are found, an empty DataFrame is returned.
    """
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the objects in the list
    for obj in obj_list:
        # Get the value of the specified attribute
        value = getattr(obj, attr)

        # Increment the count for the value
        counts[value] = counts.get(value, 0) + 1

    # Create a DataFrame from the dictionary
    df = pd.DataFrame.from_dict(counts, orient='index')

    # Rename the columns
    df.columns = ['count']

    # Sort the DataFrame by the count column
    df.sort_values(by='count', inplace=True)

    return df
class ExampleObject:
    def __init__(self, animal, shape):
        self.animal = animal
        self.shape = shape
obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]