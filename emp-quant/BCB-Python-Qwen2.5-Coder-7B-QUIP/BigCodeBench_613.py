
import pandas as pd
from matplotlib import pyplot as plt

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def task_func(goals, penalties):
    # Calculate net scores for each team
    net_scores = {team: goals[team] - penalties[team] for team in TEAMS}
    
    # Clip scores to stay within the specified range
    net_scores = {team: max(GOALS_RANGE[0], min(GOALS_RANGE[1], score)) for team, score in net_scores.items()}
    
    # Create a DataFrame with the results
    result_df = pd.DataFrame(list(net_scores.items()), columns=['Team', 'Score'])
    
    # Plot the results
    result_df.set_index('Team', inplace=True)
    result_df.plot(kind='bar', y='Score', legend=False)
    plt.ylabel('Score')
    plt.title('Team Scores')
    plt.show()
    
    # Return the DataFrame
    return result_df