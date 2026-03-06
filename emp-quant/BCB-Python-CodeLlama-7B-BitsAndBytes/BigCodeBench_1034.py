
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Create a DataFrame for each store's sales data
    df1 = pd.DataFrame(s1, columns=CATEGORIES)
    df2 = pd.DataFrame(s2, columns=CATEGORIES)

    # Compute the Euclidean distance between the two series
    dist = np.linalg.norm(df1 - df2)

    # Filter the categories where both stores have sales exceeding the threshold of 200
    mask = (df1 >= 200) & (df2 >= 200)
    categories = CATEGORIES[mask]

    # Create a bar plot for the filtered categories
    if len(categories) > 0:
        fig, ax = plt.subplots()
        ax.bar(categories, df1[categories], label=s1)
        ax.bar(categories, df2[categories], label=s2)
        ax.set_title("Sales Comparison")
        ax.set_xlabel("Categories")
        ax.set_ylabel("Sales")
        ax.legend()
        return ax
    else:
        return None

ax = task_func(s1, s2)
print(ax)
print(dist)