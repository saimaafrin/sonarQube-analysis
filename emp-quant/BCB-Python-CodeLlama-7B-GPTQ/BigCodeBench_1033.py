import itertools
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func():
    # Generate all possible 3-letter combinations of the alphabet
    combinations = itertools.product(string.ascii_lowercase, repeat=3)

    # Save the combinations in a pandas DataFrame
    df = pd.DataFrame(combinations, columns=['combination'])

    # Plot a histogram of the frequency of the first letters in the combinations
    ax = df['combination'].str[0].value_counts().plot.bar()

    # Return the DataFrame and the Axes object
    return df, ax