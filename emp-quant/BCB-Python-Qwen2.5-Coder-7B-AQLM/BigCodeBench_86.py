
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    np.random.seed(seed)
    scores = np.random.randint(0, 100, size=len(students))
    df = pd.DataFrame({'Student': students, 'Score': scores})
    df_sorted = df.sort_values(by='Score')
    
    fig, ax = plt.subplots()
    df_sorted.plot(kind='bar', x='Student', y='Score', ax=ax)
    ax.set_title('Student Scores')
    ax.set_xlabel('Student')
    ax.set_ylabel('Score')
    
    return df_sorted, ax