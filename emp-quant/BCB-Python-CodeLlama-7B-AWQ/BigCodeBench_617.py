from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    """
    Generate and analyze a Pandas DataFrame of football match results for multiple teams, incorporating random goals and penalties, then visualize the analyzed data with columns 'Team', 'Goals', and 'Penalty Cost'. Penalties are converted into fines based on a predetermined penalty cost.
    """
    # Set random seed
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize DataFrame
    df = pd.DataFrame(columns=['Team', 'Goals', 'Penalty Cost'])

    # Generate random goals and penalties
    for team in teams:
        goals = [randint(0, 10) for _ in range(goals)]
        penalties = [randint(0, 10) for _ in range(penalties)]

        # Convert penalties into fines
        fines = [PENALTY_COST * penalty for penalty in penalties]

        # Add team, goals, and penalties to DataFrame
        df = df.append({'Team': team, 'Goals': sum(goals), 'Penalty Cost': sum(fines)}, ignore_index=True)

    # Visualize DataFrame
    plt.figure(figsize=(10, 6))
    plt.bar(df['Team'], df['Goals'], label='Goals')
    plt.bar(df['Team'], df['Penalty Cost'], bottom=df['Goals'], label='Penalty Cost')
    plt.legend()
    plt.show()

    # Return DataFrame
    return df