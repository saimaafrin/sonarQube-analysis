import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
def task_func(s_list, plot_path=None):
    """
    Analyze and plot the average similarity scores of strings in a list.

    This function calculates the average similarity score of each string compared to all other strings in the list using the SequenceMatcher ratio. If a plot path is provided, it saves the plot of these scores; otherwise, it just returns the scores.

    Parameters:
    s_list (list of str): List of strings to analyze.
    plot_path (str, optional): Path to save the plot. If None, plot is not saved.

    Returns:
    list: List of average similarity scores for each string in `s_list`.

    Raises:
    ValueError: If `s_list` is not a list of strings.
    Return numpy.nan if the list contains a single element

    Requirements:
    - numpy
    - difflib
    - matplotlib.pyplot as plt

    Example:
    >>> s_list = ['apple', 'apples', 'ape', 'app', 'april']
    >>> avg_scores = task_func(s_list, 'similarity_plot.png')
    >>> expect = [0.7522727272727273, 0.6969696969696969, 0.6458333333333333, 0.6458333333333333, 0.5363636363636364]
    >>> np.all(np.isclose(avg_scores, expect, atol=1e-4))
    True
    >>> os.remove('similarity_plot.png')
    """
    if not isinstance(s_list, list):
        raise ValueError('`s_list` must be a list of strings.')
    if len(s_list) == 1:
        return np.nan
    scores = []
    for s in s_list:
        score = 0
        for t in s_list:
            if s == t:
                continue
            score += SequenceMatcher(None, s, t).ratio()
        scores.append(score / (len(s_list) - 1))
    if plot_path is not None:
        plt.plot(s_list, scores)
        plt.xlabel('String')
        plt.ylabel('Average Similarity Score')
        plt.savefig(plot_path)
        plt.close()
    return scores