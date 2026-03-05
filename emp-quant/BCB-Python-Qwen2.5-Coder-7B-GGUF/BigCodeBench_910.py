
import numpy as np
import matplotlib.pyplot as plt

def task_func(letters, repetitions, colors):
    if not letters or not repetitions or not colors:
        raise ValueError("Input lists cannot be empty")
    if len(letters) != len(repetitions) or len(letters) != len(colors):
        raise ValueError("Lengths of input lists must match")
    
    # Flatten the list by repeating each element according to the repetitions list
    flattened_list = [item for sublist in zip(letters, repetitions) for item in [sublist[0]] * sublist[1]]
    
    # Count the frequency of each letter
    letter_counts = {letter: flattened_list.count(letter) for letter in set(flattened_list)}
    
    # Prepare data for plotting
    letters = list(letter_counts.keys())
    frequencies = list(letter_counts.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(letters, frequencies, color=[colors[letters.index(letter)] for letter in letters])
    
    # Set labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    
    return ax