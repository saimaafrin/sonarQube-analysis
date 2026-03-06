
import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the dictionary has the required keys
    if not all(key in data for key in ['Name', 'Age', 'Score']):
        raise ValueError("The dictionary does not have the required keys.")

    # Create a dataframe from the dictionary
    df = pd.DataFrame(data)

    # Sort the dataframe by 'Name' and 'Age' in ascending order
    df = df.sort_values(by=['Name', 'Age'])

    # Calculate the average score per student
    avg_scores = df.groupby('Name')['Score'].mean()

    # Get the most common age
    ages = Counter(df['Age'])
    most_common_age = ages.most_common(1)[0][0] if ages else None

    return df, avg_scores, most_common_age