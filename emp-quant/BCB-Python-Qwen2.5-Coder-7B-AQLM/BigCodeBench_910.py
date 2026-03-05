
import numpy as np
import matplotlib.pyplot as plt

def task_func(letters, repetitions, colors):
    if not letters or not repetitions or not colors:
        raise ValueError("All input lists must be non-empty.")
    if len(letters) != len(repetitions) or len(letters) != len(colors):
        raise ValueError("All input lists must have the same length.")
    
    # Flatten the list by repeating each element according to its repetition count
    flattened_letters = [letter for letter, repeat in zip(letters, repetitions) for _ in range(repeat)]
    
    # Count the frequency of each letter
    letter_counts = np.unique(flattened_letters, return_counts=True)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(letter_counts[0], letter_counts[1], color=colors)
    
    # Set labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    
    return ax