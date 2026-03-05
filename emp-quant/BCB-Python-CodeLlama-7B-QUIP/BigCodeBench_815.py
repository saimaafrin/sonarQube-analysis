
import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    test_scores_df = pd.DataFrame(test_scores)

    # Calculate the average score for the student
    avg_score = test_scores_df.loc[student]['Score'].mean()

    # Calculate the standard deviation for the student
    std_dev = test_scores_df.loc[student]['Score'].std()

    # Return a numpy array containing the average score and the standard deviation
    return np.array([avg_score, std_dev])