
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Set random seed if provided
    if rng_seed:
        seed(rng_seed)
    # Generate random goals and penalties for each team
    goals = {team: randint(0, 10) for team in teams}
    penalties = {team: randint(0, 10) for team in teams}
    # Convert penalties into fines
    fines = {team: penalty * PENALTY_COST for team, penalty in penalties.items()}
    # Calculate total goals and fines
    total_goals = sum(goals.values())
    total_fines = sum(fines.values())
    # Create DataFrame
    df = pd.DataFrame({
        'Team': [team for team in teams],
        'Goals': [goals[team] for team in teams],
        'Penalty Cost': [fines[team] for team in teams]
    })
    # Visualize data
    plt.figure(figsize=(10, 6))
    plt.bar(df['Team'], df['Goals'], label='Goals')
    plt.bar(df['Team'], df['Penalty Cost'], label='Penalties')
    plt.legend()
    plt.show()
    return df