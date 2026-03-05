
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
    # Set the random seed for reproducibility
    random.seed(seed)
    # Create a list of attribute values
    attr_values = [getattr(obj, attr) for obj in obj_list]
    # Create a histogram of the attribute values
    hist, bins = np.histogram(attr_values, bins=num_bins)
    # Create a plot of the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1]-bins[0])
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    return ax