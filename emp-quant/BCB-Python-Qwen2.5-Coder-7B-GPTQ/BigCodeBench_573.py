import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)
    
    # Calculate mean, median, and standard deviation for both arrays
    stats1 = {
        'Mean': np.mean(array1),
        'Median': np.median(array1),
        'Standard Deviation': np.std(array1)
    }
    stats2 = {
        'Mean': np.mean(array2),
        'Median': np.median(array2),
        'Standard Deviation': np.std(array2)
    }
    
    # Store results in a DataFrame
    statistics = pd.DataFrame({
        'Array1': stats1,
        'Array2': stats2
    })
    
    # Draw a bar chart to compare these statistics
    statistics.T.plot(kind='bar', figsize=(10, 5))
    plt.title('Comparison of Statistics for Array1 and Array2')
    plt.xlabel('Statistics')
    plt.ylabel('Values')
    plt.show()
    
    return statistics