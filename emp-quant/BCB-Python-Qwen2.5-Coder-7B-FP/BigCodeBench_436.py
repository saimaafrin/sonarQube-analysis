import string
import matplotlib.pyplot as plt
def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Convert the string to lowercase to make the frequency count case-insensitive
    s = s.lower()
    
    # Initialize a dictionary to store the frequency of each letter
    frequency = {}
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char in string.ascii_lowercase:
            # Increment the frequency count of the character
            frequency[char] = frequency.get(char, 0) + 1
    
    # Create a bar chart of the frequencies
    fig, ax = plt.subplots()
    ax.bar(frequency.keys(), frequency.values())
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequencies')
    
    return frequency, ax