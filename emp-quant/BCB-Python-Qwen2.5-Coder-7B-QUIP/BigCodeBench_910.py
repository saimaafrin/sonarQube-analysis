
import numpy as np
import matplotlib.pyplot as plt

def task_func(letters, repetitions, colors):
    # Check if the lengths of the input lists match and are not empty
    if len(letters) != len(repetitions) or len(letters) == 0:
        raise ValueError("Input lists must have the same length and not be empty")
    
    # Flatten the list of letters by repeating each letter according to its repetition count
    flattened_letters = [letter for letter, repeat in zip(letters, repetitions) for _ in range(repeat)]
    
    # Calculate the frequency of each letter in the flattened list
    letter_counts = {letter: flattened_letters.count(letter) for letter in set(flattened_letters)}
    
    # Create a bar chart for the frequency of letters
    fig, ax = plt.subplots()
    ax.bar(range(len(letter_counts)), list(letter_counts.values()), color='blue')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    
    # Set the x-axis labels to the unique letters
    ax.set_xticks(range(len(letter_counts)))
    ax.set_xticklabels(list(letter_counts.keys()))
    
    return ax