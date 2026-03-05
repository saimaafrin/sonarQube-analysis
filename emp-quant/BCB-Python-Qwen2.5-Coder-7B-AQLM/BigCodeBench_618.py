
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate match results
    match_results = []
    for _ in range(goals):
        match_results.append({
            'Team': TEAMS[randint(0, len(TEAMS) - 1)],
            'Goals': 1,
            'Penalty Cost': 0
        })
    for _ in range(penalties):
        match_results.append({
            'Team': TEAMS[randint(0, len(TEAMS) - 1)],
            'Goals': 0,
            'Penalty Cost': PENALTY_COST
        })
    
    # Create DataFrame
    df = pd.DataFrame(match_results)
    
    # Create plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot goals
    sns.barplot(x='Team', y='Goals', data=df, ax=axes[0])
    axes[0].set_title('Goals by Team')
    axes[0].set_xlabel('Team')
    axes[0].set_ylabel('Goals')
    
    # Plot penalty costs
    sns.barplot(x='Team', y='Penalty Cost', data=df, ax=axes[1])
    axes[1].set_title('Penalty Costs by Team')
    axes[1].set_xlabel('Team')
    axes[1].set_ylabel('Penalty Cost (USD)')
    
    plt.tight_layout()
    
    return df, [axes[0], axes[1]]