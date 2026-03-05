
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(
    epoch_milliseconds,
    teams=["Team1", "Team2", "Team3", "Team4", "Team5"],
    random_seed=0,
):
    # Set random seed for reproducibility
    random.seed(random_seed)

    # Generate performance data for each team
    performance_data = {}
    for team in teams:
        performance_data[team] = []
        for i in range(epoch_milliseconds, datetime.now().timestamp()):
            performance_data[team].append(random.uniform(0.1, 1))

    # Plot performance trend
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_xlabel("Days since start")
    ax.set_ylabel("Performance")
    ax.set_title("Performance Trend")
    for team in teams:
        ax.plot(performance_data[team], label=team)
    ax.legend()
    plt.show()

    return performance_data