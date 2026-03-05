
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Generate random match results
    if rng_seed is not None:
        seed(rng_seed)
    match_results = []
    for team in teams:
        match_results.append((team, randint(0, goals), randint(0, penalties)))

    # Convert penalties into fines
    fines = []
    for team, _, penalty in match_results:
        if penalty > 0:
            fines.append((team, penalty * PENALTY_COST))

    # Create DataFrame
    df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])
    df['Fines'] = fines

    # Visualize data
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Team', y='Goals', data=df)
    sns.barplot(x='Team', y='Penalty Cost', data=df)
    plt.show()

    return df