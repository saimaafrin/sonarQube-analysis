
import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

def task_func(s_list, plot_path=None):
    if not isinstance(s_list, list):
        raise ValueError("s_list must be a list of strings")
    if len(s_list) == 1:
        return np.nan
    scores = []
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            scores.append(SequenceMatcher(None, s_list[i], s_list[j]).ratio())
    if plot_path:
        plt.plot(scores)
        plt.savefig(plot_path)
    return scores