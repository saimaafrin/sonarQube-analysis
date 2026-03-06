from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    """
    Plot a sine wave whose frequency is determined by the day of the month from the given date.

    Parameters:
    date_str (str): A date in "yyyy-mm-dd" format, used to determine the frequency of the sine wave.

    Returns:
    matplotlib.axes.Axes: An Axes object containing the plotted sine wave.

    Requirements:
    - datetime.datetime
    - numpy
    - matplotlib.pyplot

    Example:
    >>> ax = task_func('2023-06-15')
    >>> print(ax.get_title())
    Sine Wave for 2023-06-15 (Frequency: 15)
    """
    date = datetime.strptime(date_str, '%Y-%m-%d')
    freq = date.day
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x * freq)
    ax = plt.axes()
    ax.plot(x, y)
    ax.set_title(f'Sine Wave for {date_str} (Frequency: {freq})')
    return ax