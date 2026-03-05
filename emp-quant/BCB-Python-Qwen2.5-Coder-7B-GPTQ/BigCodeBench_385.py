import matplotlib.pyplot as plt
from collections import Counter
def task_func(fruit_dict):
    # Initialize a counter to keep track of fruit frequencies
    fruit_counter = Counter()
    
    # Iterate over each person's favorite fruit in the dictionary
    for fruit in fruit_dict.values():
        # Increment the count for the fruit in the counter
        fruit_counter[fruit] += 1
    
    # Extract the fruit names and their counts from the counter
    fruits = list(fruit_counter.keys())
    counts = list(fruit_counter.values())
    
    # Create a bar chart of the fruit frequencies
    fig, ax = plt.subplots()
    ax.bar(fruits, counts)
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_title('Fruit Frequency Chart')
    
    # Return the dictionary with fruit counts and the axes object of the plot
    return fruit_counter, ax