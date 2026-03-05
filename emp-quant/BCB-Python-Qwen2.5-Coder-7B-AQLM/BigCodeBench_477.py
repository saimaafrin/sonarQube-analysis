
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    np.random.seed(seed)
    
    # Ensure each category appears at least once if N >= len(CATEGORIES)
    if N >= len(CATEGORIES):
        categories = np.repeat(CATEGORIES, N // len(CATEGORIES))
        remaining = N - len(categories)
        categories = np.concatenate((categories, np.random.choice(CATEGORIES, remaining)))
    else:
        categories = np.random.choice(CATEGORIES, N, replace=False)
    
    # Shuffle the categories to ensure randomness
    np.random.shuffle(categories)
    
    # Create the DataFrame
    data = {
        "x": np.random.rand(N),
        "y": np.random.rand(N),
        "category": categories
    }
    df = pd.DataFrame(data)
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df["x"], df["y"], c=df["category"], cmap='viridis')
    plt.colorbar(scatter)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Scatter Plot of x vs y, Colored by Category")
    
    return df, ax