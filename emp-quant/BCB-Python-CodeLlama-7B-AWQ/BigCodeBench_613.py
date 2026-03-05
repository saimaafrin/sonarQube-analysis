import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)
def task_func(goals, penalties):
    """
    Calculates net scores for teams by subtracting penalties from goals and clips scores to stay within -10 to 10.
    Visualizes results with a bar chart showing each team's adjusted scores 'Team' on the x-axis and score values 'Score' on the y-axis.
    """
    # Calculate net scores
    net_scores = goals - penalties
    # Clip scores to stay within -10 to 10
    net_scores = np.clip(net_scores, *GOALS_RANGE)
    # Create DataFrame with columns 'Team' and 'Score'
    df = pd.DataFrame({'Team': TEAMS, 'Score': net_scores})
    # Visualize results
    plt.bar(df['Team'], df['Score'])
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Net Scores')
    plt.show()
    return df