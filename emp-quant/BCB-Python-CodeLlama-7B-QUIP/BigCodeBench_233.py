
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

def task_func(obj_list, attr, num_bins=30, seed=0):
    # Set random seed for reproducibility
    random.seed(seed)

    # Get the attribute values
    values = [getattr(obj, attr) for obj in obj_list]

    # Create histogram of attribute values
    counts, bins = np.histogram(values, bins=num_bins)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], counts, width=1, align='center')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of attribute values')
    return ax