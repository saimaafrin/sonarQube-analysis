
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    # Generate random goals and penalties for each team
    if rng_seed is not None:
        seed(rng_seed)
    goals = [randint(0, 10) for _ in range(len(teams))]
    penalties = [randint(0, 10) for _ in range(len(teams))]

    # Convert penalties into fines
    fines = [penalty_cost * penalty for penalty in penalties]

    # Create a DataFrame with the results
    results = pd.DataFrame({
        'Team': teams,
        'Goals': goals,
        'Penalty Cost': penalties,
        'Fine': fines
    })

    # Create a bar plot of the results
    fig, ax = plt.subplots()
    ax.bar(results['Team'], results['Goals'], label='Goals')
    ax.bar(results['Team'], results['Penalty Cost'], bottom=results['Goals'], label='Penalties')
    ax.bar(results['Team'], results['Fine'], bottom=results['Penalty Cost'], label='Fines')
    ax.set_xlabel('Team')
    ax.set_ylabel('Goals/Penalties/Fines')
    ax.legend()

    return results, ax