import collections
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(dictionary, new_key, new_value):
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value
    
    # Plot the distribution of the values in the dictionary
    values = list(dictionary.values())
    ax = sns.histplot(values, kde=True)
    
    # Set the title and labels for the plot
    ax.set_title('Distribution of Values in Dictionary')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    
    return dictionary, ax