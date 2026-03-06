
import pandas as pd
import numpy as np

def task_func(test_scores, student):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(test_scores)
    
    # Check if the student is present in the DataFrame
    if student not in df['Student'].values:
        raise ValueError("student is not present in the test_scores dataframe")
    
    # Filter the DataFrame for the specific student
    student_df = df[df['Student'] == student]
    
    # Calculate the average score and standard deviation
    avg_score = student_df['Score'].mean()
    std_dev = student_df['Score'].std()
    
    # Return the results as a numpy array and the DataFrame
    return np.array([avg_score, std_dev]), df