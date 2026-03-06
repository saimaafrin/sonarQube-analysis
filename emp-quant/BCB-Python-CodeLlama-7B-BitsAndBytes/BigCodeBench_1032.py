
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    # Generate random strings
    random_strings = [random.choice(LETTERS) for _ in range(rows)]
    for i in range(string_length - 1):
        random_strings = [random.choice(LETTERS) for _ in range(rows)]

    # Create DataFrame of random strings
    df = pd.DataFrame(random_strings, columns=['string'])

    # Calculate frequency of each letter in each string
    df['frequency'] = df['string'].str.count(LETTERS)

    # Convert DataFrame to one-hot encoded format
    df = pd.get_dummies(df, columns=['string'])

    # Calculate frequency of each letter across all strings
    df['frequency'] = df.sum(axis=0)

    # Create heatmap of correlation matrix
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    # Return heatmap object or None if no data is available
    if df.empty:
        print("No data to generate heatmap.")
        return None
    else:
        return sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Call function with specified parameters
task_func(rows=1000, string_length=3)