import random
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    """
    Draws a histogram of the "from_user" values in the provided result.
    The color of the histogram bars is selected at random from the provided colors list.
    """
    # Extract the "from_user" values from the result
    from_users = [row['from_user'] for row in result]

    # Create a histogram of the "from_user" values
    plt.hist(from_users, color=random.choice(colors))

    # Display the histogram
    plt.show()