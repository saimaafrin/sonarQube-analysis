
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate random goals and penalties for each team
    team_data = {team: {'Goals': randint(0, goals), 'Penalties': randint(0, penalties)} for team in TEAMS}
    
    # Convert penalties into fines
    for team in team_data:
        team_data[team]['Fines'] = team_data[team]['Penalties'] * PENALTY_COST
    
    # Create a DataFrame from the team data
    df = pd.DataFrame(list(team_data.values()), index=team_data.keys())
    
    # Create plots for goals and penalty costs
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot goals
    sns.barplot(x=df.index, y='Goals', data=df, ax=axes[0])
    axes[0].set_title('Goals per Team')
    axes[0].set_xlabel('Team')
    axes[0].set_ylabel('Goals')
    
    # Plot penalty costs
    sns.barplot(x=df.index, y='Fines', data=df, ax=axes[1])
    axes[1].set_title('Fines per Team')
    axes[1].set_xlabel('Team')
    axes[1].set_ylabel('Fines (in dollars)')
    
    return df, axes.tolist()