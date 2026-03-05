import seaborn as sns
import matplotlib.pyplot as plt
import random
def task_func(list_of_lists, seed=0):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Initialize an empty list to store all data
    combined_data = []
    
    # Iterate through each sublist in the list of lists
    for sublist in list_of_lists:
        # If the sublist is empty, fill it with 5 random integers between 0 and 100
        if not sublist:
            sublist = [random.randint(0, 100) for _ in range(5)]
        
        # Extend the combined data list with the current sublist
        combined_data.extend(sublist)
    
    # Create a histogram using seaborn
    ax = sns.histplot(data=combined_data, kde=False)
    
    # Return the axes object
    return ax