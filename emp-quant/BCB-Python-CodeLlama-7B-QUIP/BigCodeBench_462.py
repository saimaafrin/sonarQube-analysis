
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be greater than 0")

    # Generate random data
    random.seed(random_seed)
    data = [random.choice(categories) for _ in range(num_rows)]

    # Create DataFrame
    df = pd.DataFrame(data, columns=["category"])

    # Visualize the counts of each category
    counts = df["category"].value_counts()
    ax = plt.figure(figsize=(8, 6), dpi=100)
    ax.bar(counts.index, counts.values, color="blue", label="Category Counts")
    ax.set_title("Category Counts")
    plt.show()

    return df, ax