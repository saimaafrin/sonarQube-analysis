import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    """
    Create a numeric array of random integers, calculate the mean and standard deviation, and draw a histogram of the distribution.

    Note:
        The random integers are generated between 1 and 100. The title of the histogram is "Histogram of Random Integers". 
        The x-axis is labeled "Value" and the y-axis is labeled "Frequency". 
        The mean is plotted as a red dashed line, and the standard deviation is plotted as purple dashed lines.
        
    Returns:
    Tuple: A tuple containing the array, mean, standard deviation, and the histogram plot (Axes).

    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> array, mean, std, ax = task_func()
    >>> print(mean, std)
    49.6135 28.5323416100046
    >>> plt.show()
    """
    # Create a numeric array of random integers
    array = np.random.randint(1, 100, ARRAY_SIZE)

    # Calculate the mean and standard deviation
    mean = np.mean(array)
    std = np.std(array)

    # Draw a histogram of the distribution
    ax = plt.hist(array, bins=100, density=True, color='#000000', edgecolor='#000000', linewidth=0.5)

    # Plot the mean and standard deviation
    plt.plot([mean, mean], [0, 1], color='#FF0000', linestyle='--')
    plt.plot([mean - std, mean + std], [0, 1], color='#FF00FF', linestyle='--')

    # Set the title of the histogram
    plt.title("Histogram of Random Integers")

    # Set the x-axis label
    plt.xlabel("Value")

    # Set the y-axis label
    plt.ylabel("Frequency")

    # Return the array, mean, standard deviation, and the histogram plot
    return array, mean, std, ax