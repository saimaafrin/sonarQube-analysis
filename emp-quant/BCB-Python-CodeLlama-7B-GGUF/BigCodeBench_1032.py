
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    # Generate random strings
    random_strings = [
        ''.join(random.choice(LETTERS) for _ in range(string_length))
        for _ in range(rows)
    ]

    # Create DataFrame from random strings
    df = pd.DataFrame(random_strings)

    # Calculate frequency of each letter in each string
    df_letter_freq = df.apply(lambda x: x.value_counts())

    # Convert DataFrame to one-hot encoded format
    df_one_hot = pd.get_dummies(df_letter_freq)

    # Calculate frequency of each letter across all strings
    df_letter_freq_sum = df_one_hot.sum(axis=0)

    # Create heatmap of correlation matrix
    sns.heatmap(df_letter_freq_sum, annot=True, cmap='coolwarm')

    # Return heatmap object
    return sns.heatmap(df_letter_freq_sum, annot=True, cmap='coolwarm')