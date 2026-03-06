import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
def task_func(input_file):
    """
    Reads a JSON file containing a list of dictionaries. For each key across all dictionaries,
    calculates the mean and median of its values using numpy. Visualizes the mean and median
    using bar charts. Returns the results and plots.

    Parameters:
        - input_file (str): Path to the input JSON file containing a list of dictionaries.

    Returns:
        - result (dict): each key corresponds to those in the input dictionaries, and the corresponding
          value is another dict with keys 'mean' and 'median', representing the calculated statistics.
        - plots  (list[matplotlib.axes._axes.Axes]): A list of bar charts, one for
          each key in the dictionaries, visualizing the mean and median values.

    Requirements:
        - json
        - numpy
        - collections.defaultdict
        - matplotlib.pyplot

    Example:
    >>> results, plots = task_func("sample_data.json")
    >>> type(plots[0])
    <class 'matplotlib.axes._axes.Axes'>
    >>> results
    {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 6.0, 'median': 6.0}}
    """
    with open(input_file) as f:
        data = json.load(f)

    result = defaultdict(dict)
    plots = []
    for d in data:
        for k, v in d.items():
            result[k]['mean'] = np.mean(v)
            result[k]['median'] = np.median(v)

    for k, v in result.items():
        fig, ax = plt.subplots()
        ax.bar(x=[0, 1], height=[v['mean'], v['median']], width=0.5)
        ax.set_xticks([0, 1])
        ax.set_xticklabels([k, k])
        ax.set_title(k)
        ax.set_ylabel('value')
        ax.set_xlabel('statistic')
        ax.set_ylim([0, 10])
        ax.set_xlim([-0.5, 1.5])
        plots.append(ax)

    return result, plots