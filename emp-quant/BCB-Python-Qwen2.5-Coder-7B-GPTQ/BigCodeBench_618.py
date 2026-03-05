from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties):
    # Generate match results
    data = {
        'Team': TEAMS,
        'Goals': [randint(0, goals) for _ in TEAMS],
        'Penalty Cost': [randint(0, penalties) * PENALTY_COST for _ in TEAMS]
    }
    df = pd.DataFrame(data)
    
    # Create plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot goals
    sns.barplot(x='Team', y='Goals', data=df, ax=axes[0])
    axes[0].set_title('Goals per Team')
    axes[0].set_xlabel('Team')
    axes[0].set_ylabel('Goals')
    
    # Plot penalty costs
    sns.barplot(x='Team', y='Penalty Cost', data=df, ax=axes[1])
    axes[1].set_title('Penalty Costs per Team')
    axes[1].set_xlabel('Team')
    axes[1].set_ylabel('Penalty Cost (in dollars)')
    
    plt.tight_layout()
    plt.show()
    
    return df, axes.tolist()