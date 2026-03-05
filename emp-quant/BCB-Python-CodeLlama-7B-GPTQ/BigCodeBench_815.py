import pandas as pd
import numpy as np
def task_func(test_scores, student):
    """
    Convert a dictionary of test results into a pandas DataFrame and Calculate the average test score and the standard deviation for a particular student from this DataFrame.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)

    # Check if the student is present in the test_scores dataframe
    if student not in df['Student'].values:
        raise ValueError("student is not present in the test_scores dataframe")

    # Calculate the average test score and the standard deviation for the student
    student_scores = df[df['Student'] == student]['Score']
    average_score = student_scores.mean()
    std_dev = student_scores.std()

    # Return the numpy array containing the average score and the standard deviation for the student
    return np.array([average_score, std_dev])