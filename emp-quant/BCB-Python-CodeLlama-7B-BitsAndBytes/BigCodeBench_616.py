
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    # Generate random goals and penalties for each team
    results = []
    for team in teams:
        goals = randint(0, 10)
        penalties = randint(0, 10)
        results.append({'team': team, 'goals': goals, 'penalties': penalties})

    # Convert penalties into fines
    for result in results:
        result['fines'] = result['penalties'] * penalty_cost

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Create a bar plot of the results
    fig, ax = plt.subplots()
    ax.bar(df['team'], df['goals'], color='blue')
    ax.bar(df['team'], df['penalties'], color='red')
    ax.bar(df['team'], df['fines'], color='green')
    ax.set_xlabel('Team')
    ax.set_ylabel('Goals/Penalties/Fines')
    ax.set_title('Football Match Results')
    plt.show()

# Call the function with default parameters
task_func(goals=10, penalties=10)