
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate random match results
    results = []
    for _ in range(goals):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        goals_scored = randint(0, 10)
        penalty_cost = penalties * goals_scored
        results.append({
            'Team': team,
            'Goals': goals_scored,
            'Penalty Cost': penalty_cost
        })

    # Convert results to DataFrame
    df = pd.DataFrame(results)

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot goals
    sns.barplot(x=df['Team'], y=df['Goals'], ax=axes[0])
    axes[0].set_title('Goals per Team')
    axes[0].set_xlabel('Team')
    axes[0].set_ylabel('Goals')

    # Plot penalty costs
    sns.barplot(x=df['Team'], y=df['Penalty Cost'], ax=axes[1])
    axes[1].set_title('Penalty Costs per Team')
    axes[1].set_xlabel('Team')
    axes[1].set_ylabel('Penalty Cost')

    # Show plots
    plt.tight_layout()
    plt.show()

    return df, [axes[0], axes[1]]