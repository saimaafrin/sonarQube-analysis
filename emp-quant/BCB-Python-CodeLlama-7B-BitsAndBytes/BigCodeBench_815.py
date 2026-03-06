
import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)

    # Calculate the average test score and standard deviation for the student
    avg_score = df[df['Student'] == student]['Score'].mean()
    std_dev = df[df['Student'] == student]['Score'].std()

    # Return the numpy array containing the average score and standard deviation
    return np.array([avg_score, std_dev])

# Call the function and print the output
result = task_func(scores, student)
print(result)