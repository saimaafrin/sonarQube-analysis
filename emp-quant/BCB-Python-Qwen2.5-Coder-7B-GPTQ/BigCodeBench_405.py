import random
import matplotlib.pyplot as plt
def task_func(points: int):
    # Generate a list of random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the random numbers
    ax.plot(range(points), random_numbers)
    
    # Return the list of random numbers and the Axes object
    return random_numbers, ax