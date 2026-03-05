import pandas as pd
from collections import Counter
def task_func(data):
    """
    Analyze a dictionary of student data to return a dataframe sorted by name and age in ascending order, the average score per student as a pandas Series, and the most common age as an integer.
    The function should raise the exception for: ValueError: If the dictionary does not have the required keys.
    The function should output with:
        pd.DataFrame, pd.Series, int or None:
        A dataframe sorted by 'Name' and 'Age' in ascending order.
        A series representing average scores indexed by student names.
        An integer representing the most common age or None if no data is available.
    """
    # Check if the dictionary has the required keys
    if not all(key in data for key in ['Name', 'Age', 'Score']):
        raise ValueError("The dictionary does not have the required keys.")

    # Create a dataframe from the dictionary
    df = pd.DataFrame(data)

    # Sort the dataframe by 'Name' and 'Age' in ascending order
    df = df.sort_values(by=['Name', 'Age'])

    # Calculate the average score per student
    scores = df['Score'].mean()

    # Get the most common age
    ages = Counter(df['Age'])
    most_common_age = ages.most_common(1)[0][0] if ages else None

    return df, scores, most_common_age
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [90, 80, 70]}