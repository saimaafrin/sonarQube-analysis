
import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the required keys are present in the dictionary
    required_keys = {'Name', 'Age', 'Score'}
    if not required_keys.issubset(data):
        raise ValueError("The dictionary does not have the required keys.")

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Sort the DataFrame by 'Name' and 'Age' in ascending order
    df = df.sort_values(by=['Name', 'Age'])

    # Calculate the average score per student
    average_scores = df.groupby('Name')['Score'].mean()

    # Find the most common age
    most_common_age = df['Age'].mode().iloc[0] if not df['Age'].empty else None

    return df, average_scores, most_common_age