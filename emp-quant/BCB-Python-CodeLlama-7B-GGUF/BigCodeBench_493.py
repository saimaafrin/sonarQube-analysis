
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, teams=["Team1", "Team2", "Team3", "Team4", "Team5"], random_seed=0):
    # Generate performance data for each team
    performance_data = {}
    for team in teams:
        performance_data[team] = []
        for day in range(epoch_milliseconds, datetime.now().timestamp() * 1000):
            performance_data[team].append(random.uniform(0.1, 1))

    # Plot performance trend for each team
    fig, ax = plt.subplots()
    for team, performance in performance_data.items():
        ax.plot(performance, label=team)
    ax.set_xlabel("Days since epoch")
    ax.set_ylabel("Performance")
    ax.legend()
    return performance_data, fig