
import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Convert string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize a dictionary to store the frequency of each letter
    letter_freq = {}
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char in string.ascii_lowercase:
            # Update the frequency count for the letter
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    
    # Create a bar chart of the letter frequencies
    fig, ax = plt.subplots()
    ax.bar(letter_freq.keys(), letter_freq.values())
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequencies')
    
    return letter_freq, ax