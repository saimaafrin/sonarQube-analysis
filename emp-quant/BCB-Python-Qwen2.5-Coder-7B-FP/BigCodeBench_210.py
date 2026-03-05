import collections
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    # Count the frequency of each letter in the data
    letter_counts = collections.Counter(data)
    
    # Sort the letters by their frequency in descending order
    sorted_letters = sorted(letter_counts.items(), key=itemgetter(1), reverse=True)
    
    # Extract the letters and their counts
    letters = [letter for letter, count in sorted_letters]
    counts = [count for letter, count in sorted_letters]
    
    # Find the letter with the maximum count
    max_value_letter = letters[0]
    max_value_count = counts[0]
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(letters, counts, color='blue')
    
    # Highlight the letter with the maximum count
    ax.bar(max_value_letter, max_value_count, color='red')
    
    # Set labels and title
    ax.set_xlabel('Letter')
    ax.set_ylabel('Count')
    ax.set_title('Letter Counts with Max Value Letter Highlighted')
    
    # Add legend
    ax.legend(['Letter Counts', 'Max Value Letter'])
    
    return ax