
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the result
    from_user_values = [item['from_user'] for item in result]
    
    # Select a random color from the provided list
    color = random.choice(colors)
    
    # Draw the histogram with the selected color
    sns.histplot(from_user_values, color=color)
    
    # Display the plot
    plt.show()