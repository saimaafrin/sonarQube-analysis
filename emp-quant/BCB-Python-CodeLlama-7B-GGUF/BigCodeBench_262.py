
import collections
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(dictionary, new_key, new_value):
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value

    # Create a bar graph of the distribution of values in the dictionary
    ax = sns.barplot(x=dictionary.values())

    # Return the updated dictionary and the axes object of the bar graph
    return dictionary, ax

# Add the new key-value pair to the dictionary and plot the distribution
dictionary, ax = task_func(dictionary, new_key, new_value)

# Show the plot
plt.show()