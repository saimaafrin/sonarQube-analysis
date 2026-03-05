
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Create a histogram of the "from_user" values in the provided result
    hist, edges = np.histogram(result['from_user'], bins=50)

    # Select a random color for each bar in the histogram
    colors = random.choice(colors, len(hist))

    # Display the histogram
    fig, ax = plt.subplots()
    ax.bar(edges[:-1], hist, color=colors)
    plt.show()