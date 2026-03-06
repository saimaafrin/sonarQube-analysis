
import pandas as pd
from matplotlib import pyplot as plt

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def task_func(goals, penalties):
    # Calculate net scores for each team
    net_scores = {team: goals[team] - penalties[team] for team in TEAMS}

    # Clip scores to stay within -10 to 10
    clipped_scores = {team: min(max(score, GOALS_RANGE[0]), GOALS_RANGE[1]) for team, score in net_scores.items()}

    # Create a pandas DataFrame with columns 'Team' and 'Score'
    df = pd.DataFrame(clipped_scores, columns=['Team', 'Score'])

    # Visualize results with a bar chart
    plt.bar(df['Team'], df['Score'])
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Net Scores')
    plt.show()