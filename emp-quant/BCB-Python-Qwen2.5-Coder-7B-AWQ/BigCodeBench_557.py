import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
def task_func(s_list, plot_path=None):
    # Check if s_list is a list of strings
    if not all(isinstance(item, str) for item in s_list):
        raise ValueError("s_list must be a list of strings")
    
    # If the list contains a single element, return numpy.nan
    if len(s_list) == 1:
        return [np.nan]
    
    # Initialize a list to store the average similarity scores
    avg_scores = []
    
    # Calculate the average similarity score for each string
    for i, s1 in enumerate(s_list):
        total_score = 0
        for s2 in s_list:
            if s1 != s2:
                total_score += SequenceMatcher(None, s1, s2).ratio()
        avg_scores.append(total_score / (len(s_list) - 1))
    
    # If a plot path is provided, save the plot
    if plot_path:
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(s_list)), avg_scores, tick_label=s_list)
        plt.xlabel('String Index')
        plt.ylabel('Average Similarity Score')
        plt.title('Average Similarity Scores of Strings')
        plt.savefig(plot_path)
        plt.close()
    
    return avg_scores