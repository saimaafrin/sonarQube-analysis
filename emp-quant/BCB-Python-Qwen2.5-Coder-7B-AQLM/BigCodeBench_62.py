
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the result
    from_user_values = [item['from_user'] for item in result]
    
    # Select a random color for the histogram bars
    random_color = random.choice(colors)
    
    # Create a histogram using seaborn
    sns.histplot(from_user_values, color=random_color)
    
    # Display the histogram
    plt.show()
    
    # Return None as specified
    return None