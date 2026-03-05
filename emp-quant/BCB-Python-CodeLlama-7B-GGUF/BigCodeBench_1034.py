
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Filter categories where both stores have sales exceeding the threshold of 200
    categories = [cat for cat in CATEGORIES if s1[cat] > 200 and s2[cat] > 200]

    # Compute Euclidean distance between the two series
    dist = euclidean(s1[categories], s2[categories])

    # Generate bar plot for categories where both stores have sales exceeding the threshold
    if categories:
        fig, ax = plt.subplots()
        ax.bar(categories, s1[categories], label=s1.name)
        ax.bar(categories, s2[categories], label=s2.name)
        ax.set_title(f"{s1.name} vs {s2.name} Sales Comparison")
        ax.set_xlabel("Categories")
        ax.set_ylabel("Sales")
        ax.legend()
        return ax, dist
    else:
        return None, 0.0