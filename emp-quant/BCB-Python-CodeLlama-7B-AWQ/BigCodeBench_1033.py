import itertools
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func():
    # Generate all possible 3-letter combinations of the alphabet
    combinations = itertools.product(string.ascii_lowercase, repeat=3)

    # Create a DataFrame from the combinations
    df = pd.DataFrame(combinations, columns=['first_letter', 'second_letter', 'third_letter'])

    # Plot a histogram of the frequency of the first letters in the combinations
    ax = df['first_letter'].value_counts().plot(kind='bar')

    return df, ax