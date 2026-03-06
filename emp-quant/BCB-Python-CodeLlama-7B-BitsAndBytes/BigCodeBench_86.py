
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    np.random.seed(seed)
    scores = np.random.randint(0, 100, size=(len(students), 1))
    df = pd.DataFrame({'Student': students, 'Score': scores})
    df.sort_values(by='Score', inplace=True)
    fig, ax = plt.subplots()
    ax.bar(df['Student'], df['Score'])
    ax.set_xlabel('Student')
    ax.set_ylabel('Score')
    ax.set_title('Bar Plot of Scores')
    return df, ax