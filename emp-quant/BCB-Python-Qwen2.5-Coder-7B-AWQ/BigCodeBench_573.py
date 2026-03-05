import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)
    
    # Calculate mean, median, and standard deviation for each array
    mean1 = np.mean(array1)
    median1 = np.median(array1)
    std1 = np.std(array1)
    
    mean2 = np.mean(array2)
    median2 = np.median(array2)
    std2 = np.std(array2)
    
    # Store results in a DataFrame
    statistics = pd.DataFrame({
        'Array1': [mean1, median1, std1],
        'Array2': [mean2, median2, std2]
    }, index=['Mean', 'Median', 'Standard Deviation'])
    
    # Draw a bar chart to compare these statistics
    statistics.plot(kind='bar', figsize=(10, 5))
    plt.title('Comparison of Statistics for Two Arrays')
    plt.ylabel('Values')
    plt.show()
    
    return statistics, plt.gca()