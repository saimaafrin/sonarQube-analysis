import collections
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(dictionary, new_key, new_value):
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value
    
    # Plot the distribution of the values in the dictionary
    values = list(dictionary.values())
    ax = sns.barplot(x=range(len(values)), y=values)
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Distribution of Values in Dictionary')
    
    return dictionary, ax