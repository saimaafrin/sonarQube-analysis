import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
def task_func(s_list, plot_path=None):
    """
    Analyze and plot the average similarity scores of strings in a list.
    This function calculates the average similarity score of each string compared to all other strings in the list using the SequenceMatcher ratio.
    If a plot path is provided, it saves the plot of these scores; otherwise, it just returns the scores.
    The function should raise the exception for:
        ValueError: If `s_list` is not a list of strings.
        Return numpy.nan if the list contains a single element
    The function should output with:
        list: List of average similarity scores for each string in `s_list`.
    """
    if not isinstance(s_list, list):
        raise ValueError("`s_list` must be a list of strings.")
    if len(s_list) == 1:
        return np.nan

    # Calculate the average similarity score for each string in the list
    similarity_scores = []
    for i in range(len(s_list)):
        similarity_scores.append(np.nanmean([SequenceMatcher(None, s_list[i], s_list[j]).ratio() for j in range(len(s_list)) if j != i]))

    # Plot the similarity scores if a plot path is provided
    if plot_path:
        plt.plot(similarity_scores)
        plt.xlabel("String Index")
        plt.ylabel("Average Similarity Score")
        plt.title("Similarity Scores for Each String in the List")
        plt.savefig(plot_path)
        plt.close()

    return similarity_scores
s_list = ["apple", "banana", "orange", "mango", "pineapple"]