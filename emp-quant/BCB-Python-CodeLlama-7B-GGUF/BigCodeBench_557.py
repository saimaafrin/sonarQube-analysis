
import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

def task_func(s_list, plot_path=None):
    if not isinstance(s_list, list):
        raise ValueError("`s_list` must be a list of strings")
    if len(s_list) == 1:
        return np.nan

    similarity_scores = []
    for i, s1 in enumerate(s_list):
        for s2 in s_list[i+1:]:
            similarity_scores.append(SequenceMatcher(None, s1, s2).ratio())

    average_similarity_scores = np.mean(similarity_scores)

    if plot_path:
        plt.plot(similarity_scores)
        plt.xlabel("Index of String")
        plt.ylabel("Average Similarity Score")
        plt.title("Average Similarity Scores of Strings in `s_list`")
        plt.savefig(plot_path)
        plt.close()

    return average_similarity_scores