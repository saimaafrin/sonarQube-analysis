
import pandas as pd
from matplotlib import pyplot as plt

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def task_func(goals, penalties):
    # Calculate net scores
    net_scores = goals - penalties
    net_scores = net_scores.clip(lower=GOALS_RANGE[0], upper=GOALS_RANGE[1])

    # Create DataFrame
    df = pd.DataFrame({'Team': TEAMS, 'Score': net_scores})

    # Visualize results
    plt.bar(df['Team'], df['Score'])
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Net Scores')
    plt.show()