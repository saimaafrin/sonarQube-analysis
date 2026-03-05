
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    # Set random seed if provided
    if rng_seed:
        seed(rng_seed)
    # Generate random goals and penalties
    goals = randint(0, penalty_cost, len(teams))
    penalties = randint(0, penalty_cost, len(teams))
    # Create DataFrame
    df = pd.DataFrame({
        'Team': teams,
        'Goals': goals,
        'Penalties': penalties
    })
    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], color='blue', label='Goals')
    ax.bar(df['Team'], df['Penalties'], color='red', label='Penalties')
    ax.set_ylabel('Goals and Penalties')
    ax.set_xlabel('Teams')
    ax.set_title('Football Match Results')
    return df, fig