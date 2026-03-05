import collections
import pandas as pd
def task_func(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    This function returns a pandas Dataframe containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consist of two columns ('attribute' and 'count'), which contain the attribute and its specific count respectively.
    If no attributes are found, an empty DataFrame is returned.
    """
    # Create a dictionary to store the frequency count of each attribute
    freq_dict = {}

    # Iterate through the list of objects
    for obj in obj_list:
        # Get the value of the specified attribute for the current object
        attr_val = getattr(obj, attr)

        # Increment the frequency count of the attribute in the dictionary
        if attr_val in freq_dict:
            freq_dict[attr_val] += 1
        else:
            freq_dict[attr_val] = 1

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame.from_dict(freq_dict, orient='index')

    # Rename the columns of the DataFrame
    df.columns = ['count']

    # Return the DataFrame
    return df
obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]