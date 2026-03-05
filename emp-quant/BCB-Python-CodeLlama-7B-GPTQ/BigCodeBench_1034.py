import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]
def task_func(s1, s2):
    # Create a DataFrame with the sales data for each store
    sales_df = pd.DataFrame({
        "Store 1": s1,
        "Store 2": s2
    }, index=CATEGORIES)

    # Filter the DataFrame to only include categories where both stores have sales exceeding the threshold of 200
    filtered_df = sales_df[sales_df.gt(200).all(axis=1)]

    # Compute the Euclidean distance between the two series
    distance = np.linalg.norm(filtered_df.values - filtered_df.values.T)

    # Generate a bar plot for the categories where both stores' sales exceed the threshold of 200
    if filtered_df.shape[0] > 0:
        ax = filtered_df.plot.bar(rot=0, figsize=(10, 6))
        ax.set_title("Sales Comparison")
        ax.set_xlabel("Category")
        ax.set_ylabel("Sales")
        ax.legend(loc="upper left")
        return ax, distance
    else:
        return None, 0.0
s1 = [250, 100, 300, 200, 150]
s2 = [300, 200, 150, 250, 100]