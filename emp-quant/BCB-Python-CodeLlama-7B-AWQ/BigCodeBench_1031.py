import random
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func(n_rows=1000):
    """
    Generate a histogram of the frequency of the top 30 unique random 3-letter strings.
    The function creates random strings, each consisting of 3 letters from the lowercase English alphabet.
    It then plots a histogram showing the frequencies of the top 30 most common strings among the generated set.
    """
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")

    # Generate random strings
    random_strings = [
        "".join(random.choice(string.ascii_lowercase) for _ in range(3))
        for _ in range(n_rows)
    ]

    # Count the frequency of each string
    string_counts = pd.Series(random_strings).value_counts()

    # Filter the top 30 most common strings
    top_strings = string_counts.sort_values(ascending=False).head(30)

    # Plot the histogram
    ax = top_strings.plot.bar(title="Top 30 Most Common 3-Letter Strings")

    return ax