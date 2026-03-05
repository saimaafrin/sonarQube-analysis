import pickle
import os
import matplotlib.pyplot as plt
def task_func(numbers, file_path="save.pkl"):
    # Check if the input is a list of numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Input must be a list of numbers")
    
    # Create a figure and save it to a pickle file
    fig, ax = plt.subplots()
    ax.plot(numbers)
    plt.savefig(file_path)
    plt.close(fig)
    
    # Load the figure from the pickle file
    with open(file_path, 'rb') as f:
        loaded_fig = pickle.load(f)
    
    # Delete the pickle file
    os.remove(file_path)
    
    return loaded_fig