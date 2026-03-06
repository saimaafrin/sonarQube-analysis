
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the result
    from_users = [item['from_user'] for item in result]
    
    # Select a random color for each bar in the histogram
    selected_colors = random.choices(colors, k=len(from_users))
    
    # Create a histogram using seaborn
    sns.histplot(data=result, x='from_user', palette=selected_colors)
    
    # Display the plot
    plt.show()