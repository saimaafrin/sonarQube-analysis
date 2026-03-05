
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be greater than 0")

    random.seed(random_seed)

    data = []
    for i in range(num_rows):
        category = random.choice(categories)
        value = random.randint(1, 100)
        data.append({"category": category, "value": value})

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["category"], df["value"])
    ax.set_title("Category Counts")

    return df, ax