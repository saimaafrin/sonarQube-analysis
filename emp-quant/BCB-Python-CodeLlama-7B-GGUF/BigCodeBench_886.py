
import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the required keys are present in the dictionary
    required_keys = ['Name', 'Age', 'Score']
    if not all(key in data for key in required_keys):
        raise ValueError("Dictionary does not have the required keys")

    # Create a dataframe from the dictionary
    df = pd.DataFrame(data)

    # Sort the dataframe by 'Name' and 'Age' in ascending order
    df = df.sort_values(by=['Name', 'Age'], ascending=True)

    # Calculate the average score per student
    avg_scores = df['Score'].mean()

    # Calculate the most common age
    age_counts = Counter(df['Age'])
    most_common_age = age_counts.most_common(1)[0][0]

    return df, avg_scores, most_common_age