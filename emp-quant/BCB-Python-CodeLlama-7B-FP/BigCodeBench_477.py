import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    np.random.seed(seed)
    data = np.random.rand(N, 3)
    data[:, 0] = np.random.rand(N)
    data[:, 1] = np.random.rand(N)
    data[:, 2] = np.random.choice(CATEGORIES, N)
    df = pd.DataFrame(data, columns=["x", "y", "category"])
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], c=df["category"])
    return (df, ax)
N = 100
CATEGORIES = ["A", "B", "C", "D", "E"]
seed = 42