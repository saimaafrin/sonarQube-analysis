
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    np.random.seed(seed)
    scores = np.random.randint(0, 100, len(students))
    scores.sort()
    df = pd.DataFrame({"Student": students, "Score": scores})
    fig, ax = plt.subplots()
    ax.bar(df["Student"], df["Score"])
    return df, fig