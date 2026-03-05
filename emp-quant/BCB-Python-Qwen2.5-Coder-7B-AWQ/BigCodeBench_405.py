import random
import matplotlib.pyplot as plt
def task_func(points: int):
    # Generate a list of random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the random numbers
    ax.plot(range(points), random_numbers)
    
    # Set the title and labels
    ax.set_title('Random Numbers Plot')
    ax.set_xlabel('Indices')
    ax.set_ylabel('Generated Numbers')
    
    # Return the list of random numbers and the axes object
    return random_numbers, ax