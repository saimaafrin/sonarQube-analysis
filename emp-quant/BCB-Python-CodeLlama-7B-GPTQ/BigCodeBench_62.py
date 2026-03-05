import random
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    """
    Draws a histogram of the "from_user" values in the provided result.
    The color of the histogram bars is selected at random from the provided colors list.
    The function should output with:
        None: The function displays the histogram and does not return any value.
    """
    # Extract the "from_user" values from the result
    from_users = [row['from_user'] for row in result]

    # Create a histogram of the "from_user" values
    sns.histplot(from_users, color=random.choice(colors))

    # Display the histogram
    plt.show()
result = [
    {'from_user': 'user1', 'to_user': 'user2', 'message': 'Hello!'},
    {'from_user': 'user2', 'to_user': 'user1', 'message': 'Hi!'},
    {'from_user': 'user1', 'to_user': 'user2', 'message': 'How are you?'},
    {'from_user': 'user2', 'to_user': 'user1', 'message': 'I am good, thanks!'},
    {'from_user': 'user1', 'to_user': 'user2', 'message': 'What are you up to?'},
    {'from_user': 'user2', 'to_user': 'user1', 'message': 'I am just hanging out.'},
]