
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    # Seed the random number generator for reproducibility
    if rng_seed is not None:
        seed(rng_seed)

    # Generate random goals and penalties for each team
    results = {team: {'Goals': goals, 'Penalties': penalties} for team in TEAMS}

    # Convert penalties to fines
    for team in TEAMS:
        results[team]['Fines'] = penalties * PENALTY_COST

    # Create a DataFrame from the results
    df = pd.DataFrame(results).transpose().reset_index().rename(columns={'index': 'Team', 'Goals': 'Goals', 'Penalties': 'Penalties', 'Fines': 'Fines'})

    # Create a bar plot of the results
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Fines'], label='Fines')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Fines')
    ax.set_title('Football Match Results')
    ax.legend()

    return df, ax