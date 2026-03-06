import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    """
    Create a numeric array of random integers, calculate the mean and standard deviation, and draw a histogram of the distribution.

    Returns:
    Tuple: A tuple containing the array, mean, standard deviation, and the histogram plot (Axes).

    Note:
        The random integers are generated between 1 and 100. The title of the histogram is "Histogram of Random Values". 
        The x-axis is labeled "Val" and the y-axis is labeled "Freq". 
        The mean is plotted as a red dashed line, and the standard deviation is plotted as purple dashed lines.
        
    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> array, mean, std, ax = task_func()
    >>> print(mean, std)
    250.7154 142.85617453522966
    >>> plt.show()
    """
    # Create an array of random integers
    array = np.random.randint(1, 100, ARRAY_SIZE)

    # Calculate the mean and standard deviation
    mean = np.mean(array)
    std = np.std(array)

    # Draw a histogram of the distribution
    ax = plt.hist(array, bins=100, density=True)

    # Plot the mean and standard deviation
    plt.plot([mean], [0], 'r--')
    plt.plot([mean - std, mean + std], [0, 0], 'purple')

    # Set the title, x-axis label, and y-axis label
    plt.title("Histogram of Random Values")
    plt.xlabel("Val")
    plt.ylabel("Freq")

    # Return the array, mean, standard deviation, and the histogram plot (Axes)
    return array, mean, std, ax