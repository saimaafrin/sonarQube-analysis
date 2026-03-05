import pandas as pd
from matplotlib import pyplot as plt
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)
def task_func(goals, penalties):
    """
    Calculates net scores for teams by subtracting penalties from goals and clips scores to stay within -10 to 10.
    Visualizes results with a bar chart.

    Parameters:
    goals (list): A list of goals scored by each team.
    penalties (list): A list of penalties deducted from each team.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Team' and 'Score', representing each team's net score.
    """
    # Calculate net scores
    net_scores = [g - p for g, p in zip(goals, penalties)]
    
    # Clip scores to stay within the specified range
    net_scores = [max(GOALS_RANGE[0], min(GOALS_RANGE[1], score)) for score in net_scores]
    
    # Create DataFrame
    df = pd.DataFrame({'Team': TEAMS, 'Score': net_scores})
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(df['Team'], df['Score'], color='blue')
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Net Scores of Teams')
    plt.ylim(GOALS_RANGE)
    plt.show()
    
    return df