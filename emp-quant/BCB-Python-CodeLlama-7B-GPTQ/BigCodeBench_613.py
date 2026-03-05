import pandas as pd
import matplotlib.pyplot as plt
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)
def task_func(goals, penalties):
    # Calculate net scores for each team
    net_scores = []
    for team, goals, penalties in zip(TEAMS, goals, penalties):
        net_scores.append(goals - penalties)

    # Clip scores to stay within -10 to 10
    net_scores = [max(min(score, GOALS_RANGE[1]), GOALS_RANGE[0]) for score in net_scores]

    # Create a DataFrame with columns 'Team' and 'Score'
    df = pd.DataFrame({'Team': TEAMS, 'Score': net_scores})

    # Visualize results with a bar chart
    plt.bar(df['Team'], df['Score'])
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Net Scores')
    plt.show()
goals = [10, 5, 8, 3, 6]
penalties = [2, 1, 3, 0, 1]