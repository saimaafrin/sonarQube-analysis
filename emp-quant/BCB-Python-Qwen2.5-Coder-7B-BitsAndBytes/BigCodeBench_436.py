
import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Convert to lowercase to make the count case-insensitive
    s = s.lower()
    
    # Initialize a dictionary to store the frequency of each letter
    freq_dict = {letter: 0 for letter in string.ascii_lowercase}
    
    # Count the frequency of each letter
    for char in s:
        if char in string.ascii_lowercase:
            freq_dict[char] += 1
    
    # Filter out letters that do not appear in the string
    freq_dict = {k: v for k, v in freq_dict.items() if v > 0}
    
    # Create a bar chart of the frequencies
    fig, ax = plt.subplots()
    ax.bar(freq_dict.keys(), freq_dict.values())
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequencies')
    
    return (freq_dict, ax)