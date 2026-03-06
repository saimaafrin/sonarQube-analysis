
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate random goals and penalties for each team
    goals_dict = {}
    penalties_dict = {}
    for team in TEAMS:
        goals_dict[team] = randint(0, 10)
        penalties_dict[team] = randint(0, 10)

    # Convert penalties into fines
    fines_dict = {}
    for team, penalty in penalties_dict.items():
        fines_dict[team] = penalty * PENALTY_COST

    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Team': TEAMS,
        'Goals': goals_dict.values(),
        'Penalties': penalties_dict.values(),
        'Fines': fines_dict.values()
    })

    # Plot the results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(x='Team', y='Goals', data=df, ax=ax1)
    sns.barplot(x='Team', y='Penalties', data=df, ax=ax2)

    return df, [ax1, ax2]

# Call the function and save the results
df, [ax1, ax2] = task_func(goals=10, penalties=10)

# Save the plots
fig.savefig('football_results.png')