
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    np.random.seed(seed)
    data = pd.DataFrame({
        "x": np.random.rand(N),
        "y": np.random.rand(N),
        "category": np.random.choice(CATEGORIES, N)
    })
    fig, ax = plt.subplots()
    ax.scatter(data["x"], data["y"], c=data["category"])
    return data, ax