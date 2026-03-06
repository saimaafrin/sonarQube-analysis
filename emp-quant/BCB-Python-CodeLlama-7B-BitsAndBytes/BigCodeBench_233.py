
import random
import matplotlib.pyplot as plt

# Sample data
class Object:
    value = 0
    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value

# Function to create a histogram of the specified attribute from a list of objects
def task_func(obj_list, attr, num_bins=30, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Extract the attribute values from the objects
    attr_values = [getattr(obj, attr) for obj in obj_list]

    # Create a histogram of the attribute values
    hist, bins = np.histogram(attr_values, bins=num_bins)

    # Create a bar plot of the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])

    # Set the plot title and labels
    ax.set_title('Histogram of {} values'.format(attr))
    ax.set_xlabel('{} values'.format(attr))
    ax.set_ylabel('Count')

    # Return the histogram plot
    return ax

# Create the histogram plot
ax = task_func(obj_list, attr, num_bins, seed)

# Show the plot
plt.show()