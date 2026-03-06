import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
def task_func(duration):
    """
    Generate and draw random data in real time for the specified duration.

    Parameters:
    - duration (int): The duration in seconds for which data is to be generated and plotted.

    Returns:
    - tuple: A tuple containing two lists.
        - The first list contains timestamps (as strings) in the format '%H:%M:%S.%f'.
        - The second list contains the generated random values.

    Requirements:
    - datetime
    - time
    - random
    - matplotlib.pyplot

    Example:
    >>> type(task_func(1))
    <class 'tuple'>
    """
    # Generate timestamps
    timestamps = []
    for i in range(duration):
        timestamps.append(datetime.now().strftime('%H:%M:%S.%f'))
        time.sleep(1)

    # Generate random values
    values = []
    for i in range(duration):
        values.append(randint(0, 100))

    # Plot the data
    plt.plot(timestamps, values)
    plt.show()

    return timestamps, values