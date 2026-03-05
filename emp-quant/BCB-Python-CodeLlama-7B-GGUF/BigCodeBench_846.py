
import collections
import pandas as pd

def task_func(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    This function returns a pandas DataFrame containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consists of two columns ('attribute' and 'count'), which contain the attribute and its specific count respectively.
    If no attributes are found, an empty DataFrame is returned.
    """
    # Create a dictionary to store the frequency count of each attribute value
    attr_counts = collections.Counter()

    # Iterate over the objects in the list
    for obj in obj_list:
        # Get the value of the specified attribute from the object
        attr_value = getattr(obj, attr)

        # Increment the frequency count of the attribute value in the dictionary
        attr_counts[attr_value] += 1

    # Create a DataFrame from the dictionary
    count_df = pd.DataFrame.from_dict(attr_counts, orient='index')

    # Rename the columns of the DataFrame
    count_df.columns = ['count']
    count_df.rename(columns={'index': 'attribute'}, inplace=True)

    return count_df