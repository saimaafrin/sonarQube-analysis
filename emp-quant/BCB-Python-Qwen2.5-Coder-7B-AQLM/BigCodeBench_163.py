
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    if cols > 5:
        raise ValueError("The number of columns exceeds the number of available categories.")
    
    # Generate random data
    data = np.random.rand(rows, cols)
    categories = [f'Category {i+1}' for i in range(cols)]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=categories)
    
    # Plotting
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Stacked Bar Chart of Random Data')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()
    
    return ax