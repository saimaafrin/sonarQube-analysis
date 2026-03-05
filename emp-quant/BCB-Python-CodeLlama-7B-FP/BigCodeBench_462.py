import pandas as pd
import random
import matplotlib.pyplot as plt
def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    """
    Creates a Pandas DataFrame with specified number of rows. Each row contains a randomly selected category from the provided categories list and a random integer between 1 and 100. The function also generates a bar chart visualizing the counts of each category in the DataFrame and returns both the DataFrame and the bar chart.
    """
    if num_rows < 1:
        raise ValueError("num_rows must be greater than 1")

    # Generate random data
    random.seed(random_seed)
    data = []
    for _ in range(num_rows):
        category = random.choice(categories)
        value = random.randint(1, 100)
        data.append([category, value])

    # Create DataFrame
    df = pd.DataFrame(data, columns=["category", "value"])

    # Generate bar chart
    fig, ax = plt.subplots()
    ax.bar(df["category"], df["value"])
    ax.set_title("Category Counts")
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")

    return df, ax