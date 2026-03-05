
import random
import string
import pandas as pd

def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0")

    # Generate a list of random 3-letter strings
    random_strings = [random.choice(string.ascii_lowercase) for i in range(n_rows)]

    # Create a pandas DataFrame with the random strings
    df = pd.DataFrame(random_strings)

    # Group the DataFrame by the top 30 most frequent strings
    top_30 = df.groupby(df.values.argmax(1)).count()

    # Plot the histogram
    ax = top_30.plot.bar(figsize=(10, 10))

    return ax