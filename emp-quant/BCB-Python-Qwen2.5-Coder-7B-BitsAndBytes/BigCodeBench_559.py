
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate Euclidean distance
    euclidean_dist = distance.euclidean(a, b)
    
    # Create DataFrame
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(df['A'], label='List A')
    ax.plot(df['B'], label='List B')
    ax.legend()
    ax.set_title(f'Euclidean Distance: {euclidean_dist:.2f}')
    
    return euclidean_dist, df, ax