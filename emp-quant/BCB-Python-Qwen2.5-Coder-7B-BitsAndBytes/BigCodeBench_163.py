
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    if cols > 10:
        raise ValueError("Number of columns cannot exceed 10.")
    
    # Generate random data
    data = np.random.rand(rows, cols)
    categories = [f'Category {chr(65+i)}' for i in range(cols)]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=categories)
    
    # Plotting
    ax = df.plot(kind='bar', stacked=True)
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Stacked Bar Chart')
    plt.show()
    
    return ax