import collections
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(dictionary, new_key, new_value):
    """
    Add a new key-value pair to the dictionary and plot the distribution of its values.

    Args:
        dictionary (dict): The dictionary to add the new key-value pair to.
        new_key (str): The key to add to the dictionary.
        new_value (int): The value to add to the dictionary.

    Returns:
        dict: The updated dictionary.
        matplotlib.axes.Axes: The axes object of the plotted bar graph.
    """
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value

    # Create a bar graph of the distribution of values in the dictionary
    ax = sns.barplot(x=dictionary.values())

    # Return the updated dictionary and the axes object of the bar graph
    return dictionary, ax
dictionary = collections.Counter({'a': 1, 'b': 2, 'c': 3})
new_key = 'd'
new_value = 4