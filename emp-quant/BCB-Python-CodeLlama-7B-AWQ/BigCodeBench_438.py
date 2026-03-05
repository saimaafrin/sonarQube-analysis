import pickle
import os
import matplotlib.pyplot as plt
def task_func(numbers, file_path="save.pkl"):
    """
    Saves a Matplotlib image generated from the provided "numbers" list in a pickle file.
    The function then reads the image back from the file for validation and deletes the pickle file afterward.
    The function should raise the exception for: TypeError: If the input is not a list of numbers.
    The function should output with:
        loaded_fig (matplotlib.figure.Figure): The loaded matplotlib figure from file_path.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")

    # Generate a Matplotlib figure from the input list
    fig, ax = plt.subplots()
    ax.plot(numbers)

    # Save the figure to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(fig, f)

    # Read the figure back from the pickle file
    with open(file_path, "rb") as f:
        loaded_fig = pickle.load(f)

    # Validate the loaded figure
    if loaded_fig.axes[0].lines[0].get_data() != numbers:
        raise ValueError("Loaded figure does not match input list.")

    # Delete the pickle file
    os.remove(file_path)

    return loaded_fig
numbers = [1, 2, 3, 4, 5]