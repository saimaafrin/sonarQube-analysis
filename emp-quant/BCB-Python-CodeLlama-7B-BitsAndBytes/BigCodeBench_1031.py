
import random
import string
import pandas as pd
import matplotlib.pyplot as plt

def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")

    # Generate a list of random 3-letter strings
    letters = string.ascii_lowercase
    random_strings = [random.choice(letters) + random.choice(letters) + random.choice(letters) for _ in range(n_rows)]

    # Count the frequency of each string
    string_counts = pd.Series(random_strings).value_counts().head(30)

    # Plot the histogram
    ax = string_counts.plot(kind="bar", title="Top 30 Most Frequent 3-Letter Strings")

    return ax