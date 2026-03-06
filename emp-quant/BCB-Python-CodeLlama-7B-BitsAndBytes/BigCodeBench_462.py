
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be greater than 0")

    # Generate random category and integer data
    category_data = []
    for i in range(num_rows):
        category = random.choice(categories)
        integer_data = random.randint(1, 100)
        category_data.append([category, integer_data])

    # Create a Pandas DataFrame
    df = pd.DataFrame(category_data, columns=["category", "integer_data"])

    # Create a bar chart visualization
    fig, ax = plt.subplots()
    ax.bar(df["category"], df["integer_data"])
    ax.set_title("Category Counts")
    ax.set_xlabel("Category")
    ax.set_ylabel("Integer Data")

    return df, ax