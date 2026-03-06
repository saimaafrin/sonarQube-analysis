
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    """
    Generates a DataFrame of football match results and plots for goals and penalty costs.

    Parameters:
    goals (int): Number of goals to simulate.
    penalties (int): Number of penalties to simulate.

    Returns:
    pd.DataFrame: A dataframe containing match results.
    list: A list containing two seaborn plot objects (Axes) for goals and penalty costs.
    """
    # Generate match results
    data = {
        'Match': range(1, goals + 1),
        'Team': [randint(0, len(TEAMS) - 1) for _ in range(goals)],
        'Goals': [randint(0, 5) for _ in range(goals)],
        'Penalty Cost': [randint(0, penalties) * PENALTY_COST for _ in range(goals)]
    }
    df = pd.DataFrame(data)
    df['Team'] = df['Team'].map({i: team for i, team in enumerate(TEAMS)})
    
    # Plotting
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Goals plot
    sns.barplot(x='Match', y='Goals', hue='Team', data=df, ax=axes[0])
    axes[0].set_title('Goals per Match')
    axes[0].set_xlabel('Match')
    axes[0].set_ylabel('Goals')
    
    # Penalty Costs plot
    sns.lineplot(x='Match', y='Penalty Cost', hue='Team', data=df, marker='o', ax=axes[1])
    axes[1].set_title('Penalty Costs per Match')
    axes[1].set_xlabel('Match')
    axes[1].set_ylabel('Penalty Cost ($)')
    
    plt.tight_layout()
    return df, axes.tolist()