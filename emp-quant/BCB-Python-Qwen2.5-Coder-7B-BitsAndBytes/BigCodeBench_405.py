
import random
import matplotlib.pyplot as plt

def task_func(points: int) -> (list, plt.Axes):
    # Generate random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the data
    ax.plot(range(points), random_numbers)
    
    return random_numbers, ax