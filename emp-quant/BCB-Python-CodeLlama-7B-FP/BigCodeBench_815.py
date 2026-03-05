import pandas as pd
import numpy as np
def task_func(test_scores, student):
    """
    Convert a dictionary of test results into a pandas DataFrame and Calculate the average test score and the standard deviation for a particular student from this DataFrame.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(test_scores)

    # Check if the student is present in the DataFrame
    if student not in df['Student'].values:
        raise ValueError(f"Student {student} is not present in the test_scores dataframe")

    # Calculate the average score and the standard deviation for the student
    avg_score = df[df['Student'] == student]['Score'].mean()
    std_dev = df[df['Student'] == student]['Score'].std()

    # Return the numpy array containing the average score and the standard deviation for the student
    return np.array([avg_score, std_dev])