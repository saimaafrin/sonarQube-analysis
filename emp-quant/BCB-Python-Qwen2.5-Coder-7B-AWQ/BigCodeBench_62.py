import random
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the result
    from_user_values = [item['from_user'] for item in result]
    
    # Select a random color for the histogram bars
    random_color = random.choice(colors)
    
    # Create a histogram of the 'from_user' values
    plt.figure(figsize=(10, 6))
    sns.histplot(from_user_values, color=random_color, kde=False)
    
    # Set the title and labels
    plt.title('Histogram of from_user Values')
    plt.xlabel('from_user')
    plt.ylabel('Frequency')
    
    # Display the histogram
    plt.show()
    
    # Return None as per the requirement
    return None