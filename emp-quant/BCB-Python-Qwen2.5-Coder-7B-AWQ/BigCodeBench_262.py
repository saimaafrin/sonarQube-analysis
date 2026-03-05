import collections
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(dictionary, new_key, new_value):
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value
    
    # Create a bar graph of the dictionary values
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(dictionary.keys()), y=list(dictionary.values()))
    plt.xlabel('Keys')
    plt.ylabel('Values')
    plt.title('Distribution of Dictionary Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the updated dictionary and the axes object
    return dictionary, plt.gca()