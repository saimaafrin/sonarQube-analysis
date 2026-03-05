
import pandas as pd
from matplotlib import pyplot as plt
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)
def task_func(goals, penalties):
    # Calculate net scores
    net_scores = goals - penalties
    # Visualize results
    plt.bar(TEAMS, net_scores)
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.show()
    # Return DataFrame
    return pd.DataFrame({'Team': TEAMS, 'Score': net_scores})