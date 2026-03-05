
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Create a histogram of the "from_user" values
    sns.histplot(data=result, x="from_user", color=random.choice(colors))

    # Display the histogram
    plt.show()