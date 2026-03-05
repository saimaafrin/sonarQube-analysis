
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Seed the random number generator
    if rng_seed is not None:
        seed(rng_seed)

    # Generate random goals and penalties for each team
    results = {}
    for team in teams:
        goals_count = randint(0, goals)
        penalty_count = randint(0, penalties)
        results[team] = {'Goals': goals_count, 'Penalties': penalty_count}

    # Convert penalties to fines
    for team in results:
        results[team]['Penalty Cost'] = results[team]['Penalties'] * PENALTY_COST

    # Create a DataFrame from the results
    df = pd.DataFrame(list(results.items()), columns=['Team', 'Goals', 'Penalties', 'Penalty Cost'])

    # Print the DataFrame
    print(df)

    # Plot the results
    df.plot(x='Team', y=['Goals', 'Penalty Cost'], kind='bar', stacked=True)
    plt.ylabel('Goals and Penalty Cost')
    plt.title('Football Match Results')
    plt.show()

    return df