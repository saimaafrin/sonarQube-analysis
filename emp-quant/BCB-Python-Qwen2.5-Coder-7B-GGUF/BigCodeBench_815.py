
import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)
    
    # Check if the student is present in the DataFrame
    if student not in df['Student'].values:
        raise ValueError("student is not present in the test_scores dataframe")
    
    # Calculate the average score and standard deviation for the student
    student_scores = df[df['Student'] == student]['Score']
    average_score = np.mean(student_scores)
    std_deviation = np.std(student_scores)
    
    # Return the results as a numpy array and the DataFrame
    return np.array([average_score, std_deviation]), df