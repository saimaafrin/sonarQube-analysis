
import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    # Set the seed for random number generation
    random.seed(seed)
    
    # Fill empty sublists with 5 random integers
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend([random.randint(0, 100) for _ in range(5)])
    
    # Combine all sublists into a single list
    combined_data = [item for sublist in list_of_lists for item in sublist]
    
    # Create a histogram using seaborn
    ax = sns.histplot(combined_data, kde=True)
    
    # Return the axes object
    return ax