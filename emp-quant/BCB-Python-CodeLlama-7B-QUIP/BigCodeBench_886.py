
import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the dictionary has the required keys
    if not set(['Name', 'Age', 'Score']).issubset(set(data.keys())):
        raise ValueError("The dictionary does not have the required keys")

    # Sort the dataframe by 'Name' and 'Age' in ascending order
    df = pd.DataFrame(data).sort_values(['Name', 'Age'], ascending=True)

    # Calculate the average score for each student
    scores = df['Score'].mean()

    # Get the most common age
    ages = Counter(df['Age'])
    most_common_age = ages.most_common(1)[0][0]

    return df, scores, most_common_age