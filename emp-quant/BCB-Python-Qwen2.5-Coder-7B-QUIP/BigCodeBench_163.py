
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Generate random data
    categories = list('ABCDE')
    if cols > len(categories):
        raise ValueError("Number of columns exceeds the number of available categories.")
    data = {f'Category {i}': np.random.randint(1, 10, size=rows) for i in range(cols)}
    df = pd.DataFrame(data)
    
    # Plotting the stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Stacked Bar Chart')
    plt.show()
    
    return ax