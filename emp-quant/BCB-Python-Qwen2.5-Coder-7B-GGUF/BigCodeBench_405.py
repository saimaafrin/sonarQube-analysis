
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the random numbers
    ax.plot(range(points), random_numbers)
    
    # Set labels and title
    ax.set_xlabel('Indices')
    ax.set_ylabel('Generated Numbers')
    ax.set_title('Plot of Random Numbers')
    
    # Return the list of random numbers and the Axes object
    return random_numbers, ax