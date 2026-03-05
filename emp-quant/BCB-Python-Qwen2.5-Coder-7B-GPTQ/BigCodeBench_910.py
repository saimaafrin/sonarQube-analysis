import numpy as np
import matplotlib.pyplot as plt
def task_func(letters, repetitions, colors):
    """
    Create a bar chart to visualize the frequency of each letter in a flattened list formed by multiple repetitions of the original list.
    Each repetition of the list is associated with a different color in the chart.
    
    :param letters: List of letters to be repeated.
    :param repetitions: List of integers representing the number of repetitions for each letter.
    :param colors: List of colors corresponding to each repetition.
    :return: Matplotlib Axes object representing the created bar chart.
    """
    if not letters or not repetitions or not colors:
        raise ValueError("All input lists must be non-empty.")
    if len(letters) != len(repetitions) or len(letters) != len(colors):
        raise ValueError("The lengths of the input lists must match.")
    
    # Flatten the list by repeating each letter according to its number of repetitions
    flattened_letters = [letter for letter, repeat in zip(letters, repetitions) for _ in range(repeat)]
    
    # Count the frequency of each letter
    letter_counts = {letter: flattened_letters.count(letter) for letter in set(flattened_letters)}
    
    # Prepare data for plotting
    x = np.arange(len(letter_counts))
    heights = list(letter_counts.values())
    labels = list(letter_counts.keys())
    
    # Create bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(x, heights, color=colors)
    
    # Set labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    
    return ax