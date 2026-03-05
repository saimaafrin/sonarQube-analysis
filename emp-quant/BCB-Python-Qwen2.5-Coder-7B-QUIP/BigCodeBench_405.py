
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate a list of random numbers
    random_numbers = [random.randint(0, 100) for _ in range(points)]
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(range(points), random_numbers, 'o')
    
    # Set plot labels
    ax.set_xlabel('Index')
    ax.set_ylabel('Random Number')
    ax.set_title('Random Numbers Plot')
    
    # Return the list of random numbers and the plot
    return random_numbers, ax