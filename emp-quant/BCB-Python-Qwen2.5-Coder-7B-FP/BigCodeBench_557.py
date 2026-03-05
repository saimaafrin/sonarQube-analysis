import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
def task_func(s_list, plot_path=None):
    # Check if s_list is a list of strings
    if not all(isinstance(item, str) for item in s_list):
        raise ValueError("s_list must be a list of strings")
    
    # Check if the list contains a single element
    if len(s_list) == 1:
        return [np.nan]
    
    # Calculate the average similarity scores
    scores = []
    for i, s1 in enumerate(s_list):
        total_similarity = 0
        for s2 in s_list:
            if s1 != s2:
                total_similarity += SequenceMatcher(None, s1, s2).ratio()
        scores.append(total_similarity / (len(s_list) - 1))
    
    # Plot the scores if a plot path is provided
    if plot_path:
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(s_list)), scores, tick_label=s_list)
        plt.xlabel('String Index')
        plt.ylabel('Average Similarity Score')
        plt.title('Average Similarity Scores of Strings')
        plt.savefig(plot_path)
        plt.close()
    
    return scores