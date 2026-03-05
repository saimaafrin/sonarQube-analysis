import random
import matplotlib.pyplot as plt
def task_func(obj_list, attr, num_bins=30, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Extract the attribute values from the list of objects
    attribute_values = [getattr(obj, attr) for obj in obj_list]
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(attribute_values, bins=num_bins, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    
    # Return the histogram plot
    return ax