
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(
    epoch_milliseconds,
    teams=["Team1", "Team2", "Team3", "Team4", "Team5"],
    random_seed=0,
):
    # Convert the epoch timestamp to a datetime object
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    end_time = datetime.now()
    delta = end_time - start_time
    days = range(1, delta.days + 2)  # +1 to include the starting day

    # Initialize a dictionary to store performance data
    performance_data = {team: [] for team in teams}

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Generate random performance data for each day
    for day in days:
        for team in teams:
            performance_data[team].append(random.uniform(0.1, 1.0))

    # Create a figure and axis for plotting
    fig, ax = plt.subplots()

    # Plot the performance data for each team
    for team in teams:
        ax.plot(days, performance_data[team], label=team)

    # Set the plot title and labels
    ax.set_title('Team Performance Trend')
    ax.set_xlabel('Days since start')
    ax.set_ylabel('Performance')

    # Add a legend to the plot
    ax.legend()

    # Return the performance data and the figure object
    return performance_data, fig