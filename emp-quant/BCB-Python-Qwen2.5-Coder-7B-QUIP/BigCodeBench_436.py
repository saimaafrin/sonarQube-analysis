
import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Convert to lowercase to ensure case-insensitivity
    s = s.lower()
    
    # Initialize a dictionary to store letter frequencies
    freq_dict = {}
    
    # Iterate over each letter in the string
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    
    # Create a bar chart of the letter frequencies
    fig, ax = plt.subplots()
    ax.bar(freq_dict.keys(), freq_dict.values())
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequencies')
    
    # Return the dictionary of frequencies and the bar chart
    return freq_dict, ax