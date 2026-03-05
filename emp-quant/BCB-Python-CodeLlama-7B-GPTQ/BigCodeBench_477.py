import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    np.random.seed(seed)
    data = pd.DataFrame({
        "x": np.random.uniform(0, 10, N),
        "y": np.random.uniform(0, 10, N),
        "category": np.random.choice(CATEGORIES, N, replace=N >= len(CATEGORIES))
    })
    fig, ax = plt.subplots()
    ax.scatter(data["x"], data["y"], c=data["category"])
    return data, ax
N = 100
CATEGORIES = ["A", "B", "C", "D", "E"]