
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns
# Constants
LETTERS = list(string.ascii_lowercase)
def task_func(rows=1000, string_length=3):
    # Generate random strings
    if rows == 0:
        print("No data to generate heatmap.")
        return None
    else:
        strings = [random.choice(LETTERS) for i in range(rows)]
        # Convert strings to one-hot encoded format
        one_hot_strings = [[1 if letter in string else 0 for letter in LETTERS] for string in strings]
        # Calculate frequency of each letter
        frequency = [[sum(one_hot_string) for one_hot_string in one_hot_strings] for one_hot_strings in one_hot_strings]
        # Create DataFrame
        df = pd.DataFrame(frequency)
        # Create heatmap
        ax = sns.heatmap(df, annot=True)
        return ax